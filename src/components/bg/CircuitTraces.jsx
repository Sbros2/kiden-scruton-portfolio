import React, { useEffect, useRef } from "react";
import "./CircuitTraces.css";

export default function CircuitTraces() {
  const canvasRef = useRef(null);

  useEffect(() => {
    const canvas = canvasRef.current;
    const ctx = canvas.getContext("2d");
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;

    const traces = [
      { x1: 100, y1: 100, x2: 400, y2: 100 },
      { x1: 400, y1: 100, x2: 400, y2: 300 },
      { x1: 400, y1: 300, x2: 700, y2: 300 },
    ];

    let glowPos = 0;
    function draw() {
      ctx.clearRect(0, 0, canvas.width, canvas.height);

      ctx.strokeStyle = "#0ff3";
      ctx.lineWidth = 2;
      traces.forEach((t) => {
        ctx.beginPath();
        ctx.moveTo(t.x1, t.y1);
        ctx.lineTo(t.x2, t.y2);
        ctx.stroke();
      });

      ctx.strokeStyle = "#0ff";
      ctx.shadowBlur = 10;
      ctx.shadowColor = "#0ff";

      traces.forEach((t) => {
        const dx = t.x2 - t.x1;
        const dy = t.y2 - t.y1;
        const dist = Math.sqrt(dx * dx + dy * dy);
        const progress = glowPos % dist;
        const px = t.x1 + (dx / dist) * progress;
        const py = t.y1 + (dy / dist) * progress;

        ctx.beginPath();
        ctx.arc(px, py, 4, 0, Math.PI * 2);
        ctx.fillStyle = "#0ff";
        ctx.fill();
      });

      glowPos += 2;
      requestAnimationFrame(draw);
    }
    draw();
  }, []);

  return <canvas ref={canvasRef} className="circuit-canvas"></canvas>;
}
