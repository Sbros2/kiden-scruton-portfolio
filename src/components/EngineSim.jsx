import { useEffect, useRef, useState } from 'react';

export default function EngineSim() {
  const canvasRef = useRef(null);
  const frame = useRef(0);
  const lastTime = useRef(0);
  const phase = useRef(0);
  const [rpm, setRpm] = useState(3200);
  const [stroke, setStroke] = useState(0.72);
  const [rod, setRod] = useState(1.45);
  const [running, setRunning] = useState(true);
  const [readout, setReadout] = useState('3200 rpm');

  useEffect(() => {
    const canvas = canvasRef.current;
    const ctx = canvas.getContext('2d');

    function draw(time) {
      const rect = canvas.getBoundingClientRect();
      const ratio = window.devicePixelRatio || 1;
      canvas.width = Math.max(1, Math.floor(rect.width * ratio));
      canvas.height = Math.max(1, Math.floor(rect.height * ratio));
      ctx.setTransform(ratio, 0, 0, ratio, 0, 0);

      const delta = Math.min(0.04, (time - lastTime.current) / 1000 || 0);
      lastTime.current = time;
      if (running) phase.current += delta * rpm / 60 * Math.PI * 2;
      drawEngine(ctx, rect, phase.current, stroke, rod);
      frame.current = window.requestAnimationFrame(draw);
    }

    frame.current = window.requestAnimationFrame(draw);
    return () => window.cancelAnimationFrame(frame.current);
  }, [rpm, stroke, rod, running]);

  useEffect(() => {
    setReadout(`${Math.round(rpm).toLocaleString()} rpm / ${running ? 'running' : 'paused'}`);
  }, [rpm, running]);

  return (
    <div className="engine-sim">
      <div className="engine-toolbar">
        <button type="button" className={running ? 'is-active' : ''} onClick={() => setRunning((value) => !value)}>
          {running ? 'Pause' : 'Run'}
        </button>
        <button type="button" onClick={() => { phase.current = 0; }}>Reset phase</button>
        <span aria-live="polite">{readout}</span>
      </div>
      <canvas ref={canvasRef} className="engine-canvas" aria-label="Interactive crank-slider engine simulation" />
      <div className="engine-controls">
        <label>RPM <input type="range" min="600" max="7600" step="100" value={rpm} onChange={(event) => setRpm(Number(event.target.value))} /></label>
        <label>Stroke <input type="range" min="0.42" max="1.05" step="0.01" value={stroke} onChange={(event) => setStroke(Number(event.target.value))} /></label>
        <label>Rod length <input type="range" min="0.9" max="2.15" step="0.01" value={rod} onChange={(event) => setRod(Number(event.target.value))} /></label>
      </div>
    </div>
  );
}

function drawEngine(ctx, rect, phase, stroke, rod) {
  ctx.clearRect(0, 0, rect.width, rect.height);
  const gradient = ctx.createLinearGradient(0, 0, rect.width, rect.height);
  gradient.addColorStop(0, '#10191c');
  gradient.addColorStop(1, '#081012');
  ctx.fillStyle = gradient;
  ctx.fillRect(0, 0, rect.width, rect.height);

  const cx = rect.width * 0.5;
  const cy = rect.height * 0.62;
  const scale = Math.min(rect.width, rect.height) * 0.28;
  const crank = stroke * scale * 0.5;
  const rodLength = rod * scale;
  const bore = scale * 0.58;
  const cylinderTop = cy - rodLength - crank - scale * 0.32;
  const crankX = cx + Math.cos(phase) * crank;
  const crankY = cy + Math.sin(phase) * crank;
  const pistonY = cy - (Math.cos(phase) * crank + Math.sqrt(Math.max(0, rodLength ** 2 - (Math.sin(phase) * crank) ** 2)));
  const firing = Math.cos(phase) > 0.93;

  ctx.strokeStyle = 'rgba(124,230,196,.08)';
  ctx.lineWidth = 1;
  for (let x = 24; x < rect.width; x += 44) {
    ctx.beginPath();
    ctx.moveTo(x, 0);
    ctx.lineTo(x, rect.height);
    ctx.stroke();
  }

  roundedRect(ctx, cx - bore / 2, cylinderTop, bore, cy - cylinderTop - scale * 0.08, 10, 'rgba(141,153,167,.18)', 'rgba(237,243,241,.24)');
  roundedRect(ctx, cx - bore * 0.42, pistonY - scale * 0.14, bore * 0.84, scale * 0.28, 7, firing ? '#e4b56e' : '#8d99a7', 'rgba(237,243,241,.45)');

  ctx.strokeStyle = '#7ce6c4';
  ctx.lineWidth = 7;
  ctx.lineCap = 'round';
  ctx.beginPath();
  ctx.moveTo(cx, pistonY);
  ctx.lineTo(crankX, crankY);
  ctx.stroke();

  ctx.strokeStyle = '#e4b56e';
  ctx.lineWidth = 6;
  ctx.beginPath();
  ctx.moveTo(cx, cy);
  ctx.lineTo(crankX, crankY);
  ctx.stroke();

  ctx.strokeStyle = 'rgba(237,243,241,.35)';
  ctx.lineWidth = 5;
  ctx.beginPath();
  ctx.arc(cx, cy, crank, 0, Math.PI * 2);
  ctx.stroke();

  ctx.fillStyle = '#edf3f1';
  circle(ctx, cx, cy, 8);
  circle(ctx, crankX, crankY, 7);

  if (firing) {
    ctx.fillStyle = 'rgba(228,181,110,.22)';
    ctx.beginPath();
    ctx.moveTo(cx - bore * 0.33, cylinderTop + 16);
    ctx.lineTo(cx, cylinderTop + scale * 0.34);
    ctx.lineTo(cx + bore * 0.33, cylinderTop + 16);
    ctx.closePath();
    ctx.fill();
  }

  ctx.fillStyle = '#a5b7b9';
  ctx.font = '12px Inter, system-ui, sans-serif';
  ctx.fillText('single-cylinder crank-slider model', 18, 26);
  ctx.fillText(`stroke ${stroke.toFixed(2)} / rod ${rod.toFixed(2)}`, 18, 46);
}

function roundedRect(ctx, x, y, width, height, radius, fill, stroke) {
  ctx.beginPath();
  ctx.roundRect(x, y, width, height, radius);
  ctx.fillStyle = fill;
  ctx.fill();
  ctx.strokeStyle = stroke;
  ctx.lineWidth = 1;
  ctx.stroke();
}

function circle(ctx, x, y, radius) {
  ctx.beginPath();
  ctx.arc(x, y, radius, 0, Math.PI * 2);
  ctx.fill();
}
