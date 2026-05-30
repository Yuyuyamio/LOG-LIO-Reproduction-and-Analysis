#!/usr/bin/env python3

from pathlib import Path

INPUT = Path("results/trajectories/m2dgr_door_02_loglio_tum.txt")
OUTPUT = Path("results/figures/door_02_loglio_xy.svg")

rows = []
with INPUT.open("r", encoding="utf-8", errors="ignore") as f:
    for line in f:
        parts = line.strip().split()
        if len(parts) >= 4:
            try:
                rows.append((float(parts[1]), float(parts[2])))
            except ValueError:
                pass

if not rows:
    raise SystemExit("No valid trajectory points found.")

xs = [p[0] for p in rows]
ys = [p[1] for p in rows]

xmin, xmax = min(xs), max(xs)
ymin, ymax = min(ys), max(ys)

W, H = 900, 700
M = 70

def scale(v, vmin, vmax, out_min, out_max):
    if abs(vmax - vmin) < 1e-12:
        return (out_min + out_max) / 2
    return out_min + (v - vmin) / (vmax - vmin) * (out_max - out_min)

points = []
for x, y in rows:
    sx = scale(x, xmin, xmax, M, W - M)
    sy = scale(y, ymin, ymax, H - M, M)
    points.append(f"{sx:.2f},{sy:.2f}")

svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">
  <rect width="100%" height="100%" fill="white"/>
  <text x="{W/2}" y="35" text-anchor="middle" font-size="24" font-family="Arial">
    LOG-LIO Estimated Trajectory: M2DGR door_02
  </text>
  <line x1="{M}" y1="{H-M}" x2="{W-M}" y2="{H-M}" stroke="black"/>
  <line x1="{M}" y1="{M}" x2="{M}" y2="{H-M}" stroke="black"/>
  <text x="{W/2}" y="{H-20}" text-anchor="middle" font-size="15" font-family="Arial">x position (m)</text>
  <text x="22" y="{H/2}" text-anchor="middle" font-size="15" font-family="Arial" transform="rotate(-90 22 {H/2})">y position (m)</text>
  <polyline points="{' '.join(points)}" fill="none" stroke="black" stroke-width="2"/>
  <circle cx="{points[0].split(',')[0]}" cy="{points[0].split(',')[1]}" r="5" fill="green"/>
  <circle cx="{points[-1].split(',')[0]}" cy="{points[-1].split(',')[1]}" r="5" fill="red"/>
  <text x="{float(points[0].split(',')[0]) + 8:.2f}" y="{float(points[0].split(',')[1]) - 8:.2f}" font-size="13" font-family="Arial">Start</text>
  <text x="{float(points[-1].split(',')[0]) + 8:.2f}" y="{float(points[-1].split(',')[1]) - 8:.2f}" font-size="13" font-family="Arial">End</text>
</svg>
'''

OUTPUT.parent.mkdir(parents=True, exist_ok=True)
OUTPUT.write_text(svg, encoding="utf-8")

print(f"Input: {INPUT}")
print(f"Valid points: {len(rows)}")
print(f"Output: {OUTPUT}")
