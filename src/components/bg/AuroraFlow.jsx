import React, { useEffect, useRef } from "react";

/* Lightweight simplex-ish noise (enough for soft bands) */
function makeNoise() {
    const perm = new Uint8Array(512);
    for (let i = 0; i < 256; i++) perm[i] = perm[i + 256] = i;
    for (let i = 255; i > 0; i--) { const j = (Math.random() * 256) | 0;[perm[i], perm[j]] = [perm[j], perm[i]]; }
    const fade = t => t * t * t * (t * (t * 6 - 15) + 10);
    const lerp = (a, b, t) => a + (b - a) * t;
    const grad = (hash, x, y) => ((hash & 1) ? x : -x) + ((hash & 2) ? y : -y);
    return (x, y) => {
        const X = Math.floor(x) & 255, Y = Math.floor(y) & 255;
        x -= Math.floor(x); y -= Math.floor(y);
        const u = fade(x), v = fade(y);
        const aa = perm[perm[X] + Y], ab = perm[perm[X] + Y + 1];
        const ba = perm[perm[X + 1] + Y], bb = perm[perm[X + 1] + Y + 1];
        return lerp(
            lerp(grad(aa, x, y), grad(ba, x - 1, y), u),
            lerp(grad(ab, x, y - 1), grad(bb, x - 1, y - 1), u),
            v
        ) * 0.5 + 0.5;
    };
}

export default function AuroraFlow({ speed = 0.02, intensity = 0.7, resolution = 1.0 }) {
    const ref = useRef(null);

    useEffect(() => {
        const canvas = ref.current, ctx = canvas.getContext("2d");
        let w, h, dpr, raf;
        function resize() {
            dpr = Math.max(1, Math.min(2, window.devicePixelRatio || 1));
            w = canvas.width = Math.floor(window.innerWidth * dpr / resolution);
            h = canvas.height = Math.floor(window.innerHeight * dpr / resolution);
            canvas.style.width = window.innerWidth + "px";
            canvas.style.height = window.innerHeight + "px";
        }
        resize();
        const noise = makeNoise();

        function draw(tms) {
            const t = tms * speed;
            const img = ctx.createImageData(w, h);
            const data = img.data;
            let i = 0;
            for (let y = 0; y < h; y++) {
                for (let x = 0; x < w; x++) {
                    // layered noise -> bands
                    const nx = x / 300, ny = y / 180;
                    const n1 = noise(nx + t * 0.10, ny - t * 0.07);
                    const n2 = noise(nx * 0.6 - t * 0.03, ny * 0.6 + t * 0.05);
                    const v = Math.min(1, Math.max(0, (n1 * 0.7 + n2 * 0.6)));
                    // Cyan/teal aurora
                    const r = 15 + 40 * v * intensity;
                    const g = 120 + 120 * v * intensity;
                    const b = 110 + 140 * v * intensity;
                    data[i++] = r; data[i++] = g; data[i++] = b; data[i++] = Math.floor(255 * 0.14); // low alpha
                }
            }
            ctx.putImageData(img, 0, 0);
            raf = requestAnimationFrame(draw);
        }
        raf = requestAnimationFrame(draw);

        const ro = new ResizeObserver(resize); ro.observe(document.body);
        return () => { cancelAnimationFrame(raf); ro.disconnect(); };
    }, [speed, intensity, resolution]);

    return (
        <canvas
            ref={ref}
            style={{ position: "fixed", inset: 0, zIndex: -2, mixBlendMode: "screen", pointerEvents: "none" }}
        />
    );
}
