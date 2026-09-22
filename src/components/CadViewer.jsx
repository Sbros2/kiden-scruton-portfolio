import { useEffect, useMemo, useRef, useState } from 'react';

const MODEL_LIBRARY = {
  fanParts: {
    label: 'Fan print set',
    type: 'multi-part STL',
    note: 'Real STL exports from the retro-industrial fan project. The parts are shown together as a print/export set; use Explode to separate blades, housing, and stand for inspection.',
    camera: { x: -0.7, y: 0.56, zoom: 1.08 },
    files: [
      { url: '/models/fan-stand.stl', format: 'stl', color: '#627382', move: [0, -0.5, 0], explode: [-0.7, -0.2, 0] },
      { url: '/models/fan-housing.stl', format: 'stl', color: '#9aa7b5', move: [0, 0.1, 0], explode: [0, 0.2, 0] },
      { url: '/models/fan-blades.stl', format: 'stl', color: '#7ce6c4', move: [0, 0.72, 0], explode: [0.7, 0.55, 0] },
    ],
  },
  fanStandObj: {
    label: 'Fan stand OBJ',
    type: 'OBJ mesh',
    note: 'Wavefront OBJ version of the fan stand, included to prove the viewer supports both STL and OBJ assets.',
    camera: { x: -0.72, y: 0.74, zoom: 1.22 },
    files: [{ url: '/models/fan-stand.obj', format: 'obj', color: '#e4b56e', move: [0, 0, 0], explode: [0, 0, 0] }],
  },
  fanBlades: {
    label: 'Fan blades',
    type: 'STL mesh',
    note: 'Single STL export for inspecting the blade geometry without the rest of the fan.',
    camera: { x: -0.78, y: 0.36, zoom: 1.36 },
    files: [{ url: '/models/fan-blades.stl', format: 'stl', color: '#7ce6c4', move: [0, 0, 0], explode: [0, 0, 0] }],
  },
  monorailPrints: {
    label: 'Monorail print set',
    type: 'multi-part STL',
    note: 'STL exports from the Brennan-inspired monorail prototype: motor mount, motor adapter, flywheel, and flywheel adapter. This is a grouped parts board for inspection, not a solved dynamic assembly.',
    camera: { x: -0.65, y: 0.62, zoom: 1.25 },
    files: [
      { url: '/models/monorail-motor-mount.stl', format: 'stl', color: '#8d99a7', move: [-1.05, 0.15, 0], explode: [-0.5, 0.1, 0] },
      { url: '/models/monorail-motor-adapter.stl', format: 'stl', color: '#7ce6c4', move: [-0.25, -0.1, 0], explode: [-0.15, -0.25, 0] },
      { url: '/models/monorail-flywheel.stl', format: 'stl', color: '#e4b56e', move: [0.55, 0.05, 0], explode: [0.25, 0.25, 0] },
      { url: '/models/monorail-flywheel-adapter.stl', format: 'stl', color: '#b987ff', move: [1.05, -0.22, 0], explode: [0.65, -0.2, 0] },
    ],
  },
  splitHub: {
    label: 'Split hub clamp',
    type: 'STL mesh',
    note: 'CAD coursework mesh for a split hub clamp. This adds a compact mechanical part with holes, clamp geometry, and a different scale than the fan models.',
    camera: { x: -0.58, y: 0.8, zoom: 1.35 },
    files: [{ url: '/models/split-hub-clamp-assembly.stl', format: 'stl', color: '#7ce6c4', move: [0, 0, 0], explode: [0, 0, 0] }],
  },
  filamentHolder: {
    label: 'Filament holder',
    type: 'STL mesh',
    note: 'Makerspace utility part: a 3D-printer filament holder exported as STL. It helps the lab page show practical shop work, not only class projects.',
    camera: { x: -0.72, y: 0.48, zoom: 1.18 },
    files: [{ url: '/models/filament-holder.stl', format: 'stl', color: '#65b7ff', move: [0, 0, 0], explode: [0, 0, 0] }],
  },
  marksSpear: {
    label: 'Personal 3D model',
    type: 'STL mesh',
    note: 'Personal modeling archive mesh. It adds a non-course model to the viewer and shows that the portfolio can handle miscellaneous STL assets too.',
    camera: { x: -0.6, y: 0.64, zoom: 1.2 },
    files: [{ url: '/models/marks-spear.stl', format: 'stl', color: '#ff9f7c', move: [0, 0, 0], explode: [0, 0, 0] }],
  },
};

function parseBinaryStl(buffer, file, partIndex) {
  const view = new DataView(buffer);
  const count = view.getUint32(80, true);
  const triangles = [];
  let cursor = 84;
  for (let i = 0; i < count && cursor + 50 <= buffer.byteLength; i += 1) {
    const normal = [view.getFloat32(cursor, true), view.getFloat32(cursor + 4, true), view.getFloat32(cursor + 8, true)];
    cursor += 12;
    const points = [];
    for (let v = 0; v < 3; v += 1) {
      points.push([
        view.getFloat32(cursor, true),
        view.getFloat32(cursor + 4, true),
        view.getFloat32(cursor + 8, true),
      ]);
      cursor += 12;
    }
    triangles.push({ points, normal, color: file.color, partIndex, move: file.move, explode: file.explode });
    cursor += 2;
  }
  return triangles;
}

function parseAsciiStl(text, file, partIndex) {
  const values = Array.from(text.matchAll(/vertex\s+([^\s]+)\s+([^\s]+)\s+([^\s]+)/gi), (match) => [
    Number(match[1]), Number(match[2]), Number(match[3]),
  ]);
  const triangles = [];
  for (let i = 0; i + 2 < values.length; i += 3) {
    const points = [values[i], values[i + 1], values[i + 2]];
    triangles.push({ points, normal: triangleNormal(points), color: file.color, partIndex, move: file.move, explode: file.explode });
  }
  return triangles;
}

function parseObj(text, file, partIndex) {
  const vertices = [];
  const triangles = [];
  text.split(/\r?\n/).forEach((line) => {
    const trimmed = line.trim();
    if (trimmed.startsWith('v ')) {
      const [, x, y, z] = trimmed.split(/\s+/);
      vertices.push([Number(x), Number(y), Number(z)]);
    }
    if (trimmed.startsWith('f ')) {
      const indices = trimmed.slice(2).trim().split(/\s+/).map((token) => Number(token.split('/')[0]) - 1);
      for (let i = 1; i + 1 < indices.length; i += 1) {
        const points = [vertices[indices[0]], vertices[indices[i]], vertices[indices[i + 1]]].filter(Boolean);
        if (points.length === 3) triangles.push({ points, normal: triangleNormal(points), color: file.color, partIndex, move: file.move, explode: file.explode });
      }
    }
  });
  return triangles;
}

function triangleNormal(points) {
  const [a, b, c] = points;
  const u = [b[0] - a[0], b[1] - a[1], b[2] - a[2]];
  const v = [c[0] - a[0], c[1] - a[1], c[2] - a[2]];
  return normalize([
    u[1] * v[2] - u[2] * v[1],
    u[2] * v[0] - u[0] * v[2],
    u[0] * v[1] - u[1] * v[0],
  ]);
}

function normalize(vector) {
  const length = Math.hypot(vector[0], vector[1], vector[2]) || 1;
  return [vector[0] / length, vector[1] / length, vector[2] / length];
}

function rotatePoint([x, y, z], rx, ry) {
  const cx = Math.cos(rx);
  const sx = Math.sin(rx);
  const cy = Math.cos(ry);
  const sy = Math.sin(ry);
  const y1 = y * cx - z * sx;
  const z1 = y * sx + z * cx;
  const x2 = x * cy + z1 * sy;
  const z2 = -x * sy + z1 * cy;
  return [x2, y1, z2];
}

function shadeColor(hex, amount) {
  const value = Number.parseInt(hex.slice(1), 16);
  const r = Math.max(0, Math.min(255, (value >> 16) + amount));
  const g = Math.max(0, Math.min(255, ((value >> 8) & 255) + amount));
  const b = Math.max(0, Math.min(255, (value & 255) + amount));
  return `rgb(${r},${g},${b})`;
}

function normalizeTriangles(triangles) {
  const points = triangles.flatMap((triangle) => triangle.points);
  const min = [Infinity, Infinity, Infinity];
  const max = [-Infinity, -Infinity, -Infinity];
  points.forEach((point) => {
    for (let axis = 0; axis < 3; axis += 1) {
      min[axis] = Math.min(min[axis], point[axis]);
      max[axis] = Math.max(max[axis], point[axis]);
    }
  });
  const center = min.map((value, axis) => (value + max[axis]) / 2);
  const size = Math.max(max[0] - min[0], max[1] - min[1], max[2] - min[2]) || 1;
  return triangles.map((triangle) => ({
    ...triangle,
    points: triangle.points.map((point) => [
      ((point[0] - center[0]) / size) * 3.2 + triangle.move[0],
      ((point[2] - center[2]) / size) * 3.2 + triangle.move[1],
      ((point[1] - center[1]) / size) * 3.2 + triangle.move[2],
    ]),
  }));
}

async function loadModel(model) {
  const meshes = await Promise.all(model.files.map(async (file, partIndex) => {
    const response = await fetch(file.url);
    if (!response.ok) throw new Error(`Could not load ${file.url}`);
    if (file.format === 'obj') return parseObj(await response.text(), file, partIndex);
    const buffer = await response.arrayBuffer();
    const view = new DataView(buffer);
    const binaryCount = buffer.byteLength >= 84 ? view.getUint32(80, true) : 0;
    const expectedBinarySize = 84 + binaryCount * 50;
    if (expectedBinarySize !== buffer.byteLength) {
      const text = new TextDecoder().decode(buffer);
      const asciiTriangles = parseAsciiStl(text, file, partIndex);
      if (asciiTriangles.length) return asciiTriangles;
    }
    return parseBinaryStl(buffer, file, partIndex);
  }));
  return normalizeTriangles(meshes.flat());
}

export default function CadViewer() {
  const canvasRef = useRef(null);
  const drag = useRef(null);
  const labels = useMemo(() => Object.entries(MODEL_LIBRARY), []);
  const [modelKey, setModelKey] = useState('fanParts');
  const [rotation, setRotation] = useState(MODEL_LIBRARY.fanParts.camera);
  const [explode, setExplode] = useState(0.18);
  const [triangles, setTriangles] = useState([]);
  const [status, setStatus] = useState('Loading mesh files...');
  const model = MODEL_LIBRARY[modelKey];

  useEffect(() => {
    let cancelled = false;
    setRotation(MODEL_LIBRARY[modelKey].camera);
    setExplode(MODEL_LIBRARY[modelKey].files.length > 1 ? 0.18 : 0);
    setStatus('Loading mesh files...');
    loadModel(MODEL_LIBRARY[modelKey])
      .then((loaded) => {
        if (!cancelled) {
          setTriangles(loaded);
          setStatus(`${loaded.length.toLocaleString()} triangles · ${MODEL_LIBRARY[modelKey].type}`);
        }
      })
      .catch((error) => {
        if (!cancelled) setStatus(error.message);
      });
    return () => { cancelled = true; };
  }, [modelKey]);

  useEffect(() => {
    const canvas = canvasRef.current;
    if (!canvas) return;
    const draw = () => {
      const ctx = canvas.getContext('2d');
      const ratio = window.devicePixelRatio || 1;
      const rect = canvas.getBoundingClientRect();
      canvas.width = Math.max(1, Math.floor(rect.width * ratio));
      canvas.height = Math.max(1, Math.floor(rect.height * ratio));
      ctx.setTransform(ratio, 0, 0, ratio, 0, 0);
      drawScene(ctx, rect, triangles, rotation, explode);
    };
    draw();
    window.addEventListener('resize', draw);
    return () => window.removeEventListener('resize', draw);
  }, [triangles, rotation, explode]);

  function onPointerDown(event) {
    event.currentTarget.setPointerCapture(event.pointerId);
    drag.current = { x: event.clientX, y: event.clientY, rotation };
  }

  function onPointerMove(event) {
    if (!drag.current) return;
    const dx = event.clientX - drag.current.x;
    const dy = event.clientY - drag.current.y;
    setRotation({
      ...rotation,
      x: drag.current.rotation.x + dy * 0.01,
      y: drag.current.rotation.y + dx * 0.01,
    });
  }

  function onPointerUp() { drag.current = null; }

  return (
    <div className="cad-viewer-shell">
      <div className="cad-viewer-toolbar" aria-label="3D model controls">
        {labels.map(([key, item]) => (
          <button key={key} type="button" className={key === modelKey ? 'is-active' : ''} onClick={() => setModelKey(key)}>
            {item.label}
          </button>
        ))}
      </div>
      <div className="cad-canvas-wrap">
        <canvas
          ref={canvasRef}
          className="cad-canvas"
          aria-label={`Interactive mesh viewer showing ${model.label}`}
          onPointerDown={onPointerDown}
          onPointerMove={onPointerMove}
          onPointerUp={onPointerUp}
          onPointerCancel={onPointerUp}
        />
        <div className="cad-viewer-hud">
          <strong>{model.label}</strong>
          <span>{status}</span>
          <span>Drag to rotate · zoom below</span>
        </div>
      </div>
      <div className="cad-viewer-controls">
        <label>
          Explode
          <input type="range" min="0" max="1" step="0.05" value={explode} onChange={(event) => setExplode(Number(event.target.value))} />
        </label>
        <div>
          <button type="button" onClick={() => setRotation((value) => ({ ...value, zoom: Math.max(0.65, value.zoom - 0.12) }))}>-</button>
          <button type="button" onClick={() => setRotation((value) => ({ ...value, zoom: Math.min(1.9, value.zoom + 0.12) }))}>+</button>
          <button type="button" onClick={() => setRotation(MODEL_LIBRARY[modelKey].camera)}>Reset</button>
        </div>
      </div>
      <p className="cad-viewer-note">{model.note}</p>
    </div>
  );
}

function drawScene(ctx, rect, triangles, rotation, explode) {
  ctx.clearRect(0, 0, rect.width, rect.height);
  const gradient = ctx.createLinearGradient(0, 0, rect.width, rect.height);
  gradient.addColorStop(0, '#10191c');
  gradient.addColorStop(1, '#081012');
  ctx.fillStyle = gradient;
  ctx.fillRect(0, 0, rect.width, rect.height);

  ctx.strokeStyle = 'rgba(124,230,196,.08)';
  ctx.lineWidth = 1;
  for (let x = 24; x < rect.width; x += 42) {
    ctx.beginPath(); ctx.moveTo(x, 0); ctx.lineTo(x, rect.height); ctx.stroke();
  }
  for (let y = 24; y < rect.height; y += 42) {
    ctx.beginPath(); ctx.moveTo(0, y); ctx.lineTo(rect.width, y); ctx.stroke();
  }

  const centerX = rect.width / 2;
  const centerY = rect.height / 2 + 8;
  const scale = Math.min(rect.width, rect.height) * 0.34 * rotation.zoom;
  const light = normalize([0.35, 0.7, 0.6]);

  const projected = triangles.map((triangle) => {
    const pushed = triangle.points.map((point) => [
      point[0] + triangle.explode[0] * explode,
      point[1] + triangle.explode[1] * explode,
      point[2] + triangle.explode[2] * explode,
    ]);
    const normal = triangleNormal(pushed);
    const rotatedNormal = rotatePoint(normal, rotation.x, rotation.y);
    const brightness = Math.max(0.08, rotatedNormal[0] * light[0] + rotatedNormal[1] * light[1] + rotatedNormal[2] * light[2]);
    const points = pushed.map((point) => {
      const [x, y, z] = rotatePoint(point, rotation.x, rotation.y);
      const depth = 5.5 + z;
      const perspective = 5.5 / depth;
      return { x: centerX + x * scale * perspective, y: centerY - y * scale * perspective, z };
    });
    return {
      points,
      depth: points.reduce((sum, point) => sum + point.z, 0) / points.length,
      color: shadeColor(triangle.color, Math.round((brightness - 0.45) * 75)),
    };
  }).sort((a, b) => a.depth - b.depth);

  projected.forEach((triangle) => {
    ctx.beginPath();
    triangle.points.forEach((point, index) => {
      if (index === 0) ctx.moveTo(point.x, point.y);
      else ctx.lineTo(point.x, point.y);
    });
    ctx.closePath();
    ctx.fillStyle = triangle.color;
    ctx.fill();
    ctx.strokeStyle = 'rgba(237,243,241,.12)';
    ctx.stroke();
  });
}
