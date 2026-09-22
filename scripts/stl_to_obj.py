from __future__ import annotations

import struct
import sys
from pathlib import Path


def read_binary_stl(path: Path) -> list[tuple[tuple[float, float, float], tuple[float, float, float], tuple[float, float, float]]]:
    data = path.read_bytes()
    if len(data) < 84:
        raise ValueError("STL file is too small.")
    count = struct.unpack_from("<I", data, 80)[0]
    expected = 84 + count * 50
    if expected > len(data):
        raise ValueError("Binary STL triangle count does not match file size.")
    triangles = []
    offset = 84
    for _ in range(count):
        offset += 12
        vertices = []
        for _vertex in range(3):
            vertices.append(struct.unpack_from("<fff", data, offset))
            offset += 12
        triangles.append(tuple(vertices))
        offset += 2
    return triangles


def write_obj(triangles, destination: Path) -> None:
    vertices: list[tuple[float, float, float]] = []
    index: dict[tuple[float, float, float], int] = {}
    faces = []
    for triangle in triangles:
        face = []
        for vertex in triangle:
            key = tuple(round(value, 6) for value in vertex)
            if key not in index:
                index[key] = len(vertices) + 1
                vertices.append(key)
            face.append(index[key])
        faces.append(face)

    lines = ["# Converted from user STL for the portfolio CAD viewer."]
    lines.extend(f"v {x:.6f} {y:.6f} {z:.6f}" for x, y, z in vertices)
    lines.extend(f"f {a} {b} {c}" for a, b, c in faces)
    destination.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    source = Path(sys.argv[1])
    destination = Path(sys.argv[2])
    write_obj(read_binary_stl(source), destination)


if __name__ == "__main__":
    main()
