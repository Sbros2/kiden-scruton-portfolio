import React, { useEffect, useMemo, useRef, useState } from "react";

function rk4Step(state, dt, params) {
    const f = (x) => {
        const phi = x[0];
        const phiDot = x[1];

        const Ib = params.Ib;
        const Is = params.Is;
        const omega = params.omega;
        const Kp = params.Kp;
        const Kd = params.Kd;
        const mgh = params.mgh;

        const gravityCoeff = mgh / Ib;
        const controlDamping = (2 * Is * omega * Kd) / Ib;
        const controlStiffness = (2 * Is * omega * Kp) / Ib;

        const phiDDot =
            gravityCoeff * Math.sin(phi)
            - controlDamping * phiDot
            - controlStiffness * phi;

        return [phiDot, phiDDot];
    };

    const k1 = f(state);
    const k2 = f([state[0] + 0.5 * dt * k1[0], state[1] + 0.5 * dt * k1[1]]);
    const k3 = f([state[0] + 0.5 * dt * k2[0], state[1] + 0.5 * dt * k2[1]]);
    const k4 = f([state[0] + dt * k3[0], state[1] + dt * k3[1]]);

    return [
        state[0] + (dt / 6) * (k1[0] + 2 * k2[0] + 2 * k3[0] + k4[0]),
        state[1] + (dt / 6) * (k1[1] + 2 * k2[1] + 2 * k3[1] + k4[1]),
    ];
}

function simulate(params) {
    const dt = params.dt;
    const totalTime = params.totalTime;
    const steps = Math.floor(totalTime / dt);

    let state = [
        (params.phi0Deg * Math.PI) / 180,
        (params.phiDot0Deg * Math.PI) / 180,
    ];

    const points = [];
    for (let i = 0; i <= steps; i++) {
        const t = i * dt;

        points.push({
            t,
            phiRad: state[0],
            phiDeg: (state[0] * 180) / Math.PI,
            phiDotRad: state[1],
            phiDotDeg: (state[1] * 180) / Math.PI,
        });

        // Resolve fast damping modes even when the display sample interval is coarse.
        const rate = (2 * params.Is * params.omega * Math.abs(params.Kd)) / params.Ib
            + Math.sqrt((2 * params.Is * params.omega * Math.abs(params.Kp) + params.mgh) / params.Ib);
        const substeps = Math.max(1, Math.ceil(dt * rate / 0.5));
        if (substeps * steps > 500000) { points.error = 'These settings exceed the interactive model range. Reduce flywheel inertia, speed, damping, or duration.'; break; }
        if (Math.abs(state[0]) >= Math.PI / 2) { points.fallen = true; break; }
        for (let n = 0; n < substeps; n++) state = rk4Step(state, dt / substeps, params);

        if (!Number.isFinite(state[0]) || !Number.isFinite(state[1])) {
            break;
        }
    }

    return points;
}

function classifyResponse(params, points) {
    if (points.error) return points.error;
    if (points.fallen) return 'Stopped at 90° lean: outside the upright model';
    if (!points.length) return "No Data";

    const maxAbsAngle = Math.max(...points.map((p) => Math.abs(p.phiDeg)));

    if (maxAbsAngle > 90) {
        return "Diverging / Falls Over";
    }

    const Ib = params.Ib;
    const Is = params.Is;
    const omega = params.omega;
    const Kp = params.Kp;
    const Kd = params.Kd;
    const mgh = params.mgh;

    const gravityCoeff = mgh / Ib;
    const controlStiffness = (2 * Is * omega * Kp) / Ib;
    const controlDamping = (2 * Is * omega * Kd) / Ib;

    const netLinearizedStiffness = controlStiffness - gravityCoeff;

    if (omega <= 0 || Is <= 0 || Kp <= 0) {
        return "Unstable Upright";
    }

    if (netLinearizedStiffness <= 0) {
        return "Insufficient Righting Torque";
    }

    const zeta =
        controlDamping / (2 * Math.sqrt(Math.max(netLinearizedStiffness, 1e-9)));

    if (zeta < 0) return "Unstable, Negative Damping";
    if (zeta === 0) return "Undamped Oscillation";
    if (Math.abs(zeta - 1) < 0.05) return "Stabilized, Near Critical";
    if (zeta < 1) return "Stabilized, Underdamped";
    return "Stabilized, Overdamped";
}

function drawTimePlot(canvas, points, valueKey, yLabel, color) {
    if (!canvas || !points.length) return;
    const ctx = canvas.getContext("2d");
    const w = canvas.width;
    const h = canvas.height;

    ctx.clearRect(0, 0, w, h);
    ctx.fillStyle = "#0f141b";
    ctx.fillRect(0, 0, w, h);

    const left = 55;
    const right = 20;
    const top = 20;
    const bottom = 35;
    const pw = w - left - right;
    const ph = h - top - bottom;

    ctx.strokeStyle = "#263241";
    ctx.lineWidth = 1;

    for (let i = 0; i <= 5; i++) {
        const x = left + (i / 5) * pw;
        ctx.beginPath();
        ctx.moveTo(x, top);
        ctx.lineTo(x, top + ph);
        ctx.stroke();
    }

    for (let i = 0; i <= 4; i++) {
        const y = top + (i / 4) * ph;
        ctx.beginPath();
        ctx.moveTo(left, y);
        ctx.lineTo(left + pw, y);
        ctx.stroke();
    }

    const tMax = points[points.length - 1].t || 1;

    let yMin = Infinity;
    let yMax = -Infinity;
    for (const p of points) {
        yMin = Math.min(yMin, p[valueKey]);
        yMax = Math.max(yMax, p[valueKey]);
    }

    if (Math.abs(yMax - yMin) < 1e-6) {
        yMax += 1;
        yMin -= 1;
    }

    const yPad = 0.1 * (yMax - yMin);
    yMax += yPad;
    yMin -= yPad;

    const xMap = (t) => left + (t / tMax) * pw;
    const yMap = (v) => top + ph - ((v - yMin) / (yMax - yMin)) * ph;

    ctx.strokeStyle = color;
    ctx.lineWidth = 2;
    ctx.beginPath();
    points.forEach((p, i) => {
        const x = xMap(p.t);
        const y = yMap(p[valueKey]);
        if (i === 0) ctx.moveTo(x, y);
        else ctx.lineTo(x, y);
    });
    ctx.stroke();

    if (yMin < 0 && yMax > 0) {
        ctx.strokeStyle = "#6b7280";
        ctx.lineWidth = 1;
        const zeroY = yMap(0);
        ctx.beginPath();
        ctx.moveTo(left, zeroY);
        ctx.lineTo(left + pw, zeroY);
        ctx.stroke();
    }

    ctx.fillStyle = "#a9b4c2";
    ctx.font = "12px Arial";
    ctx.fillText(yLabel, 8, 14);
    ctx.fillText("Time (s)", w - 55, h - 8);
}

function drawPhasePlot(canvas, points) {
    if (!canvas || !points.length) return;
    const ctx = canvas.getContext("2d");
    const w = canvas.width;
    const h = canvas.height;

    ctx.clearRect(0, 0, w, h);
    ctx.fillStyle = "#0f141b";
    ctx.fillRect(0, 0, w, h);

    const left = 55;
    const right = 20;
    const top = 20;
    const bottom = 40;
    const pw = w - left - right;
    const ph = h - top - bottom;

    ctx.strokeStyle = "#263241";
    ctx.lineWidth = 1;

    for (let i = 0; i <= 5; i++) {
        const x = left + (i / 5) * pw;
        ctx.beginPath();
        ctx.moveTo(x, top);
        ctx.lineTo(x, top + ph);
        ctx.stroke();
    }

    for (let i = 0; i <= 4; i++) {
        const y = top + (i / 4) * ph;
        ctx.beginPath();
        ctx.moveTo(left, y);
        ctx.lineTo(left + pw, y);
        ctx.stroke();
    }

    let xMin = Infinity;
    let xMax = -Infinity;
    let yMin = Infinity;
    let yMax = -Infinity;

    for (const p of points) {
        xMin = Math.min(xMin, p.phiDeg);
        xMax = Math.max(xMax, p.phiDeg);
        yMin = Math.min(yMin, p.phiDotDeg);
        yMax = Math.max(yMax, p.phiDotDeg);
    }

    if (Math.abs(xMax - xMin) < 1e-6) {
        xMax += 1;
        xMin -= 1;
    }
    if (Math.abs(yMax - yMin) < 1e-6) {
        yMax += 1;
        yMin -= 1;
    }

    const xPad = 0.1 * (xMax - xMin);
    const yPad = 0.1 * (yMax - yMin);
    xMax += xPad;
    xMin -= xPad;
    yMax += yPad;
    yMin -= yPad;

    const xMap = (v) => left + ((v - xMin) / (xMax - xMin)) * pw;
    const yMap = (v) => top + ph - ((v - yMin) / (yMax - yMin)) * ph;

    if (xMin < 0 && xMax > 0) {
        ctx.strokeStyle = "#6b7280";
        ctx.beginPath();
        ctx.moveTo(xMap(0), top);
        ctx.lineTo(xMap(0), top + ph);
        ctx.stroke();
    }

    if (yMin < 0 && yMax > 0) {
        ctx.strokeStyle = "#6b7280";
        ctx.beginPath();
        ctx.moveTo(left, yMap(0));
        ctx.lineTo(left + pw, yMap(0));
        ctx.stroke();
    }

    ctx.strokeStyle = "#f59e0b";
    ctx.lineWidth = 2;
    ctx.beginPath();
    points.forEach((p, i) => {
        const x = xMap(p.phiDeg);
        const y = yMap(p.phiDotDeg);
        if (i === 0) ctx.moveTo(x, y);
        else ctx.lineTo(x, y);
    });
    ctx.stroke();

    ctx.fillStyle = "#a9b4c2";
    ctx.font = "12px Arial";
    ctx.fillText("Angular Velocity (deg/s)", 8, 14);
    ctx.fillText("Angle (deg)", w - 75, h - 8);
}

function drawPrototypeView(canvas, angleDeg) {
    if (!canvas) return;
    const ctx = canvas.getContext("2d");
    const w = canvas.width;
    const h = canvas.height;

    ctx.clearRect(0, 0, w, h);
    ctx.fillStyle = "#0f141b";
    ctx.fillRect(0, 0, w, h);

    const angleRad = (angleDeg * Math.PI) / 180;

    const groundY = h * 0.82;
    const pivotX = w / 2;
    const pivotY = groundY;

    ctx.strokeStyle = "#263241";
    ctx.lineWidth = 1.2;
    ctx.beginPath();
    ctx.moveTo(pivotX, groundY);
    ctx.lineTo(pivotX, groundY - 170);
    ctx.stroke();

    ctx.strokeStyle = "#6b7280";
    ctx.lineWidth = 2;
    ctx.beginPath();
    ctx.moveTo(28, groundY);
    ctx.lineTo(w - 28, groundY);
    ctx.stroke();

    ctx.save();
    ctx.translate(pivotX, pivotY);
    ctx.rotate(angleRad);

    const frameY = -46;
    const frameHalfWidth = 66;
    const frameHeight = 8;

    const flywheelY = -78;
    const flywheelOffset = 58;

    const flywheelRx = 18;
    const flywheelRy = 7;

    const mastWidth = 6;

    const electronicsY = -70;
    const electronicsW = 34;
    const electronicsH = 18;

    ctx.fillStyle = "#a8b4c3";
    ctx.fillRect(-frameHalfWidth, frameY, frameHalfWidth * 2, frameHeight);

    ctx.fillStyle = "#7c8796";
    ctx.fillRect(-frameHalfWidth, frameY + frameHeight - 2, frameHalfWidth * 2, 2);

    ctx.strokeStyle = "#facc15";
    ctx.lineWidth = 4;
    ctx.beginPath();
    ctx.moveTo(0, frameY + frameHeight / 2);
    ctx.lineTo(0, 0);
    ctx.stroke();

    ctx.fillStyle = "#334155";
    ctx.fillRect(-electronicsW / 2, electronicsY, electronicsW, electronicsH);

    ctx.fillStyle = "#475569";
    ctx.fillRect(-12, electronicsY - 10, 24, 8);

    ctx.fillStyle = "#64748b";
    ctx.fillRect(-flywheelOffset - mastWidth / 2, flywheelY + 6, mastWidth, 28);
    ctx.fillRect(flywheelOffset - mastWidth / 2, flywheelY + 6, mastWidth, 28);

    ctx.strokeStyle = "#7b8794";
    ctx.lineWidth = 3;
    ctx.beginPath();
    ctx.moveTo(-42, frameY + 3);
    ctx.lineTo(-flywheelOffset, frameY + 3);
    ctx.moveTo(42, frameY + 3);
    ctx.lineTo(flywheelOffset, frameY + 3);
    ctx.stroke();

    ctx.fillStyle = "#d7dee7";
    ctx.beginPath();
    ctx.ellipse(-flywheelOffset, flywheelY, flywheelRx, flywheelRy, 0.15, 0, Math.PI * 2);
    ctx.fill();

    ctx.strokeStyle = "#96a3b3";
    ctx.lineWidth = 1.5;
    ctx.beginPath();
    ctx.ellipse(-flywheelOffset, flywheelY, flywheelRx * 0.68, flywheelRy * 0.68, 0.15, 0, Math.PI * 2);
    ctx.stroke();

    ctx.fillStyle = "#d7dee7";
    ctx.beginPath();
    ctx.ellipse(flywheelOffset, flywheelY, flywheelRx, flywheelRy, -0.15, 0, Math.PI * 2);
    ctx.fill();

    ctx.strokeStyle = "#96a3b3";
    ctx.lineWidth = 1.5;
    ctx.beginPath();
    ctx.ellipse(flywheelOffset, flywheelY, flywheelRx * 0.68, flywheelRy * 0.68, -0.15, 0, Math.PI * 2);
    ctx.stroke();

    ctx.fillStyle = "#475569";
    ctx.beginPath();
    ctx.arc(-flywheelOffset, flywheelY, 2.8, 0, Math.PI * 2);
    ctx.arc(flywheelOffset, flywheelY, 2.8, 0, Math.PI * 2);
    ctx.fill();

    ctx.restore();

    ctx.fillStyle = "#e8eef5";
    ctx.beginPath();
    ctx.arc(pivotX, pivotY, 4, 0, Math.PI * 2);
    ctx.fill();

    ctx.fillStyle = "#a9b4c2";
    ctx.font = "14px Arial";
    ctx.fillText(`Lean Angle: ${angleDeg.toFixed(2)} deg`, 14, 22);
    ctx.fillText("Stylized Front View of Prototype", 14, 42);
}

function drawTopView(canvas, angleDeg) {
    if (!canvas) return;
    const ctx = canvas.getContext("2d");
    const w = canvas.width;
    const h = canvas.height;

    ctx.clearRect(0, 0, w, h);
    ctx.fillStyle = "#0f141b";
    ctx.fillRect(0, 0, w, h);

    const angleRad = (angleDeg * Math.PI) / 180;

    const cx = w / 2;
    const cy = h / 2;

    // Upright reference, top-view tilt direction
    ctx.strokeStyle = "#263241";
    ctx.lineWidth = 1.2;
    ctx.beginPath();
    ctx.moveTo(cx, 22);
    ctx.lineTo(cx, h - 22);
    ctx.stroke();

    ctx.strokeStyle = "#263241";
    ctx.beginPath();
    ctx.moveTo(22, cy);
    ctx.lineTo(w - 22, cy);
    ctx.stroke();

    ctx.save();
    ctx.translate(cx, cy);
    ctx.rotate(angleRad);

    const spineLen = 95;
    const flywheelOffset = 52;
    const flywheelRx = 11;
    const flywheelRy = 26;

    // Main center spine, perpendicular to front-view pendulum plane
    ctx.fillStyle = "#a8b4c3";
    ctx.fillRect(-6, -spineLen / 2, 12, spineLen);

    // Center block
    ctx.fillStyle = "#334155";
    ctx.fillRect(-16, -18, 32, 36);

    // Left flywheel, top view
    ctx.fillStyle = "#d7dee7";
    ctx.beginPath();
    ctx.ellipse(-flywheelOffset, 0, flywheelRx, flywheelRy, 0, 0, Math.PI * 2);
    ctx.fill();

    ctx.strokeStyle = "#96a3b3";
    ctx.lineWidth = 1.5;
    ctx.beginPath();
    ctx.ellipse(-flywheelOffset, 0, flywheelRx * 0.7, flywheelRy * 0.7, 0, 0, Math.PI * 2);
    ctx.stroke();

    // Right flywheel, top view
    ctx.fillStyle = "#d7dee7";
    ctx.beginPath();
    ctx.ellipse(flywheelOffset, 0, flywheelRx, flywheelRy, 0, 0, Math.PI * 2);
    ctx.fill();

    ctx.strokeStyle = "#96a3b3";
    ctx.lineWidth = 1.5;
    ctx.beginPath();
    ctx.ellipse(flywheelOffset, 0, flywheelRx * 0.7, flywheelRy * 0.7, 0, 0, Math.PI * 2);
    ctx.stroke();

    // Connectors
    ctx.strokeStyle = "#7b8794";
    ctx.lineWidth = 3;
    ctx.beginPath();
    ctx.moveTo(-flywheelOffset + 11, 0);
    ctx.lineTo(-10, 0);
    ctx.moveTo(10, 0);
    ctx.lineTo(flywheelOffset - 11, 0);
    ctx.stroke();

    // Yellow tilt direction line from center, top view
    ctx.strokeStyle = "#facc15";
    ctx.lineWidth = 4;
    ctx.beginPath();
    ctx.moveTo(0, 0);
    ctx.lineTo(0, spineLen / 2 + 26);
    ctx.stroke();

    ctx.restore();

    ctx.fillStyle = "#a9b4c2";
    ctx.font = "14px Arial";
    ctx.fillText(`Top View Tilt: ${angleDeg.toFixed(2)} deg`, 14, 22);
    ctx.fillText("Flywheels Above, Tilt Perpendicular to Upright Pendulum Plane", 14, 42);
}

export default function GyroSim() {
    const [params, setParams] = useState({
        Ib: 0.1022,
        Is: 0.003,
        omega: 628,
        Kp: 3,
        Kd: 0.01,
        mgh: 6,
        phi0Deg: 20,
        phiDot0Deg: 0,
        dt: 0.01,
        totalTime: 10,
    });

    const [playhead, setPlayhead] = useState(0);
    const [playing, setPlaying] = useState(false);

    const prototypeViewRef = useRef(null);
    const topViewRef = useRef(null);
    const anglePlotRef = useRef(null);
    const velocityPlotRef = useRef(null);
    const phasePlotRef = useRef(null);

    const points = useMemo(() => simulate(params), [params]);
    const responseType = useMemo(() => classifyResponse(params, points), [params, points]);

    useEffect(() => {
        drawTimePlot(anglePlotRef.current, points, "phiDeg", "Angle (deg)", "#7cc4ff");
        drawTimePlot(
            velocityPlotRef.current,
            points,
            "phiDotDeg",
            "Angular Velocity (deg/s)",
            "#22c55e"
        );
        drawPhasePlot(phasePlotRef.current, points);
    }, [points]);

    useEffect(() => {
        const idx = Math.min(playhead, Math.max(points.length - 1, 0));
        const angle = points[idx] ? points[idx].phiDeg : params.phi0Deg;
        drawPrototypeView(prototypeViewRef.current, angle);
        drawTopView(topViewRef.current, angle);
    }, [points, playhead, params.phi0Deg]);

    useEffect(() => {
        if (!playing) return;
        const start = performance.now() - playhead * params.dt * 1000;
        let frame;
        const tick = (now) => {
            const next = Math.min(points.length - 1, Math.floor((now - start) / (params.dt * 1000)));
            setPlayhead(next);
            if (next >= points.length - 1) setPlaying(false);
            else frame = requestAnimationFrame(tick);
        };
        frame = requestAnimationFrame(tick);
        return () => cancelAnimationFrame(frame);
    }, [playing, points, params.dt]);

    const setField = (key, value) => {
        setParams((prev) => ({ ...prev, [key]: value }));
        setPlayhead(0);
        setPlaying(false);
    };

    return (
        <div style={styles.wrap}>
            <div style={styles.controls}>
                <h3 style={styles.h3}>Interactive ODE Simulation</h3>
                <p style={styles.small}>
                    Adjust the controls, then play the response. The plots show the full computed run.
                </p>

                <Slider
                    label="Initial Angle (deg)"
                    min={-270}
                    max={270}
                    step={1}
                    value={params.phi0Deg}
                    onChange={(v) => setField("phi0Deg", v)}
                />

                <Slider
                    label="Initial Angular Velocity (deg/s)"
                    min={-5000}
                    max={5000}
                    step={10}
                    value={params.phiDot0Deg}
                    onChange={(v) => setField("phiDot0Deg", v)}
                />

                <Slider
                    label="Righting Gain, Kp"
                    min={-5}
                    max={25}
                    step={0.01}
                    value={params.Kp}
                    onChange={(v) => setField("Kp", v)}
                />

                <Slider
                    label="Damping Gain, Kd"
                    min={-0.05}
                    max={2.5}
                    step={0.001}
                    value={params.Kd}
                    onChange={(v) => setField("Kd", v)}
                />

                <Slider
                    label="Flywheel Speed (rad/s)"
                    min={0}
                    max={4000}
                    step={1}
                    value={params.omega}
                    onChange={(v) => setField("omega", v)}
                />

                <Slider
                    label="Total Vehicle MOI, Ib"
                    min={0.01}
                    max={2.0}
                    step={0.0001}
                    value={params.Ib}
                    onChange={(v) => setField("Ib", v)}
                />

                <Slider
                    label="Single Flywheel MOI, Is"
                    min={0}
                    max={0.2}
                    step={0.0001}
                    value={params.Is}
                    onChange={(v) => setField("Is", v)}
                />

                <Slider
                    label="Gravity / CG Term, mgh"
                    min={0}
                    max={60}
                    step={0.01}
                    value={params.mgh}
                    onChange={(v) => setField("mgh", v)}
                />

                <Slider
                    label="Time Step (s)"
                    min={0.001}
                    max={0.05}
                    step={0.001}
                    value={params.dt}
                    onChange={(v) => setField("dt", v)}
                />

                <Slider
                    label="Simulation Duration (s)"
                    min={1}
                    max={30}
                    step={0.5}
                    value={params.totalTime}
                    onChange={(v) => setField("totalTime", v)}
                />

                <div style={styles.buttonRow}>
                    <button
                        style={styles.button}
                        disabled={!!points.error}
                        onClick={() => {
                            if (playhead >= points.length - 1) setPlayhead(0);
                            setPlaying(!playing);
                        }}
                    >
                        {playing ? 'Pause' : playhead >= points.length - 1 ? 'Replay' : 'Play'}
                    </button>
                    <button
                        style={styles.button}
                        onClick={() => {
                            setPlayhead(0);
                            setPlaying(false);
                        }}
                    >
                        Reset
                    </button>
                </div>

                <div style={styles.status}>
                    <strong>Response Type:</strong> {responseType}
                    <p data-sim-time>Time: {(points[playhead]?.t || 0).toFixed(2)} s · Lean: {(points[playhead]?.phiDeg || 0).toFixed(2)}°</p>
                    <label>Playback position<input style={styles.input} aria-label="Playback position" type="range" min="0" max={Math.max(0,points.length-1)} value={playhead} onChange={e=>{setPlaying(false);setPlayhead(Number(e.target.value));}} /></label>
                </div>
            </div>

            <div style={styles.viz}>
                <div style={styles.grid2}>
                    <canvas ref={prototypeViewRef} width={370} height={260} style={styles.canvas} />
                    <div style={styles.small}><h3>What you are seeing</h3><p>The front view follows the computed roll angle. The flywheels are schematic; their spin and precession are not animated.</p><p>Model: Iᵦ φ″ = mgh sin φ − 2 Iₛ ω (Kp φ + Kd φ′).</p><p>The run stops at a 90° lean. Actual hardware also depends on actuator torque, travel, and speed control.</p></div>
                </div>

                <div style={styles.grid2}>
                    <canvas ref={anglePlotRef} width={370} height={260} style={styles.canvas} />
                    <canvas ref={velocityPlotRef} width={370} height={260} style={styles.canvas} />
                </div>

                <canvas ref={phasePlotRef} width={760} height={300} style={styles.canvas} />
            </div>
        </div>
    );
}

function Slider({ label, min, max, step, value, onChange }) {
    const wrapperRef = React.useRef(null);
    const wheelStateRef = React.useRef({
        lastTime: 0,
        burst: 0,
    });

    const decimals =
        step < 1 ? Math.min(4, String(step).split(".")[1]?.length || 2) : 0;

    const [draftValue, setDraftValue] = React.useState(String(value));

    React.useEffect(() => {
        setDraftValue(String(Number(value).toFixed(decimals)));
    }, [value, decimals]);

    const commitValue = () => {
        const parsed = draftValue.trim() === '' ? NaN : Number(draftValue);
        const next = Number.isFinite(parsed) ? Math.min(max, Math.max(min, parsed)) : value;
        setDraftValue(String(Number(next).toFixed(decimals)));
        onChange(next);
    };

    React.useEffect(() => {
        const el = wrapperRef.current;
        if (!el) return;

        const handleWheel = (e) => {
            if (!el.contains(document.activeElement)) return;
            e.preventDefault();
            e.stopPropagation();

            const now = performance.now();
            const state = wheelStateRef.current;
            const dt = now - state.lastTime;

            if (dt > 230) {
                state.burst = 0;
            }

            state.burst += 1;
            state.lastTime = now;

            let multiplier = 1;

            if (dt < 20 && state.burst >= 15) {
                multiplier = 100;
            } else if (dt < 40 && state.burst >= 5) {
                multiplier = 10;
            }

            const direction = e.deltaY > 0 ? -1 : 1;
            const next = value + direction * step * multiplier;
            const clamped = Math.min(max, Math.max(min, next));

            onChange(Number(clamped.toFixed(decimals)));
        };

        el.addEventListener("wheel", handleWheel, { passive: false });

        return () => {
            el.removeEventListener("wheel", handleWheel);
        };
    }, [value, min, max, step, onChange, decimals]);

    return (
        <div ref={wrapperRef} style={styles.label}>
            <div style={styles.labelRow}>
                <span>{label}</span>
                <input
                    style={styles.valueInput}
                    type="text"
                    aria-label={label}
                    inputMode="decimal"
                    value={draftValue}
                    onChange={(e) => setDraftValue(e.target.value)}
                    onBlur={commitValue}
                    onKeyDown={(e) => {
                        if (e.key === "Enter") {
                            commitValue();
                            e.currentTarget.blur();
                        }
                    }}
                />
            </div>
            <input
                style={styles.input}
                type="range"
                aria-label={`${label} slider`}
                min={min}
                max={max}
                step={step}
                value={Math.min(max, Math.max(min, value))}
                onChange={(e) => onChange(parseFloat(e.target.value))}
            />
        </div>
    );
}

const styles = {
    wrap: {
        display: "grid",
        gridTemplateColumns: "repeat(auto-fit, minmax(min(100%, 320px), 1fr))",
        gap: "20px",
        margin: "24px 0",
    },
    controls: {
        background: "#121821",
        border: "1px solid #263241",
        borderRadius: "14px",
        padding: "18px",
        color: "#e8eef5",
        alignSelf: "start",
    },
    viz: {
        display: "grid",
        gap: "16px",
    },
    grid2: {
        display: "grid",
        gridTemplateColumns: "repeat(auto-fit, minmax(min(100%, 240px), 1fr))",
        gap: "16px",
    },
    canvas: {
        width: "100%",
        height: "auto",
        background: "#0f141b",
        border: "1px solid #263241",
        borderRadius: "14px",
    },
    h3: {
        marginTop: 0,
        marginBottom: "8px",
    },
    small: {
        color: "#a9b4c2",
        marginTop: 0,
        marginBottom: "16px",
        fontSize: "0.95rem",
    },
    label: {
        display: "block",
        marginBottom: "12px",
        userSelect: "none",
    },
    labelRow: {
        display: "flex",
        justifyContent: "space-between",
        alignItems: "center",
        marginBottom: "6px",
        fontSize: "0.92rem",
        gap: "10px",
    },
    valueInput: {
        width: "88px",
        background: "#0f141b",
        color: "#e8eef5",
        border: "1px solid #263241",
        borderRadius: "6px",
        padding: "4px 8px",
        textAlign: "right",
        fontSize: "0.92rem",
    },
    input: {
        width: "100%",
        cursor: "ew-resize",
    },
    buttonRow: {
        display: "flex",
        gap: "10px",
        marginTop: "14px",
    },
    button: {
        background: "#7cc4ff",
        color: "#08111a",
        border: 0,
        borderRadius: "10px",
        padding: "10px 14px",
        cursor: "pointer",
        fontWeight: 700,
    },
    status: {
        marginTop: "14px",
        color: "#a9b4c2",
    },
};
