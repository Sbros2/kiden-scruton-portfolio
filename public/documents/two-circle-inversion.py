import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter

# Inversion function
def invert(P, O, r):
    vec = P - O
    d2 = np.dot(vec, vec)
    return O + (r**2 / d2) * vec

# Find a circle through exactly three points
def find_circle_through_3_points(p1, p2, p3):
    A = np.array([
        [p1[0], p1[1], 1],
        [p2[0], p2[1], 1],
        [p3[0], p3[1], 1]
    ])
    B = np.array([
        -(p1[0]**2 + p1[1]**2),
        -(p2[0]**2 + p2[1]**2),
        -(p3[0]**2 + p3[1]**2)
    ])
    sol = np.linalg.solve(A, B)
    xc = -0.5 * sol[0]
    yc = -0.5 * sol[1]
    r = np.sqrt((sol[0]**2 + sol[1]**2) / 4 - sol[2])
    return xc, yc, r

# Circle setup
radius = 1.0
a = 0.4  # Distance from origin to center

O1 = np.array([-a, 0.0])  # Circle A center
O2 = np.array([ a, 0.0])  # Circle B center

# Starting point
P0 = np.array([2, 0.05])

# Create trajectory
points = [P0]
P = P0
for i in range(100):
    if i % 2 == 0:
        P = invert(P, O1, radius)
    else:
        P = invert(P, O2, radius)
    points.append(P)

points = np.array(points)

# Fit a circle through the first three points
xc, yc, rc = find_circle_through_3_points(points[0], points[1], points[2])

# Plot setup
fig, ax = plt.subplots()
ax.set_aspect('equal')
ax.set_xlim(-4, 4)
ax.set_ylim(-2, 2)

# Draw inversion circles
circle1 = plt.Circle(O1, radius, fill=False, linestyle='--', color='black')
circle2 = plt.Circle(O2, radius, fill=False, linestyle='--', color='black')
ax.add_artist(circle1)
ax.add_artist(circle2)

# Draw trace circle (from first three points)
trace_circle = plt.Circle((xc, yc), rc, fill=False, linestyle=':', color='gray')
ax.add_artist(trace_circle)

# Moving point and path
trail, = ax.plot([], [], 'b.-')
moving_dot, = ax.plot([], [], 'ro')

# New: Line showing direction from current circle center
angle_line, = ax.plot([], [], 'g-', linewidth=1)

# Title and labels
plt.title("Point Inversion Between Two Circles Showing Angle Drop and Trace Circle")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)

def init():
    trail.set_data([], [])
    moving_dot.set_data([], [])
    angle_line.set_data([], [])
    return trail, moving_dot, angle_line

def update(frame):
    # Update trail and moving dot
    trail.set_data(points[:frame+1, 0], points[:frame+1, 1])
    moving_dot.set_data(points[frame, 0], points[frame, 1])

    # Determine which circle we're inverting about
    if frame % 2 == 0:
        center = O1
    else:
        center = O2

    # Draw line from center to point
    angle_line.set_data([center[0], points[frame, 0]],
                        [center[1], points[frame, 1]])

    return trail, moving_dot, angle_line

ani = FuncAnimation(fig, update, frames=len(points),
                    init_func=init, blit=True, interval=300)

# Save the animation
gif_path = r"C:\Users\kiden\OneDrive - University of Hartford\Documents\Hartford Assignments\.CURRENT Semester 6\Circ Invert project\Presentation\circle_inversion_with_angle_and_3pt_trace.gif"
ani.save(gif_path, writer=PillowWriter(fps=3))

print(f"GIF saved successfully to:\n{gif_path}")
