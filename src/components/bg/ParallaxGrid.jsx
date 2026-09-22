import React, { useEffect, useRef } from "react";

export default function ParallaxGrid({ opacity = 0.80 }) {
    const ref = useRef(null);

    useEffect(() => {
        const c = ref.current, ctx = c.getContext("2d");
        let w, h, dpr, raf;
        const cols = 22, rows = 12, nodes = [];
        function resize() {
            dpr = Math.max(1, Math.min(2, window.devicePixelRatio || 1));
            w = c.width = Math.floor(window.innerWidth * dpr);
            h = c.height = Math.floor(window.innerHeight * dpr);
            c.style.width = window.innerWidth + "px";
            c.style.height = window.innerHeight + "px";
        }
        function init() {
            nodes.length = 0;
            for (let y = 0; y < rows; y++) {
                for (let x = 0; x < cols; x++) {
                    nodes.push({ x: (x + 0.5) * (w / cols), y: (y + 0.5) * (h / rows), ph: Math.random() * 6.283 });
                }
            }
        }
        resize(); init();
        let mx = 0, my = 0, sx = 0, sy = 0;
        const onMove = e => {
            const X = e.clientX ?? (e.touches?.[0]?.clientX || 0);
            const Y = e.clientY ?? (e.touches?.[0]?.clientY || 0);
            mx = X / window.innerWidth - .5;
            my = Y / window.innerHeight - .5;
        };
        window.addEventListener("pointermove", onMove, { passive: true });

        function draw(t) {
            ctx.clearRect(0, 0, w, h);
            ctx.globalAlpha = opacity;
            sx += (mx * 22 - sx) * 0.04; sy += (my * 15 - sy) * 0.04;
            ctx.strokeStyle = "rgba(29,233,182,0.12)"; ctx.lineWidth = 1 * dpr; ctx.beginPath();
            for (let i = 0; i < nodes.length; i++) {
                const n = nodes[i];
                const x = n.x + sx, y = n.y + sy + Math.sin(t * 0.0005 + n.ph) * 2 * dpr;
                const col = i % cols, row = (i / cols) | 0;
                if (col < cols - 1) { const m = nodes[i + 1]; ctx.moveTo(x, y); ctx.lineTo(m.x + sx, m.y + sy); }
                if (row < rows - 1) { const m = nodes[i + cols]; ctx.moveTo(x, y); ctx.lineTo(m.x + sx, m.y + sy); }
            }
            ctx.stroke();
            for (let i = 0; i < nodes.length; i++) {
                const n = nodes[i];
                const x = n.x + sx, y = n.y + sy;
                const r = 3.1 * dpr + Math.max(0, Math.sin(t * 0.002 + n.ph)) * 0.7 * dpr;
                ctx.fillStyle = "rgba(29,233,182,0.22)"; ctx.beginPath(); ctx.arc(x, y, r, 0, 6.283); ctx.fill();
            }
            raf = requestAnimationFrame(draw);
        }
        raf = requestAnimationFrame(draw);
        const ro = new ResizeObserver(() => { resize(); init(); }); ro.observe(document.body);
        return () => { cancelAnimationFrame(raf); window.removeEventListener("pointermove", onMove); ro.disconnect(); };
    }, [opacity]);

    return <canvas ref={ref} aria-hidden="true" style={{ position: "fixed", inset: 0, zIndex: -1, pointerEvents: "none" }} />;
}
