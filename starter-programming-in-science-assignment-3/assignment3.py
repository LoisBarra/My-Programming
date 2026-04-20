import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d import Axes3D  # needed for 3D plotting


# ==================================================
# PART 0 - STUDENT ID PERSONALIZATION
# ==================================================

student_id = "2532120"

# Get the second last digit and last digit
d1 = int(student_id[-2])
d2 = int(student_id[-1])

# Compute the required values
k = (d1 + d2) % 4 + 2
shift = d1 - d2
n_points = 20 + d1
frame_step = d2 + 1

# Print the values at the start of the program
print("Student ID:", student_id)
print("d1 =", d1)
print("d2 =", d2)
print("k =", k)
print("shift =", shift)
print("n_points =", n_points)
print("frame_step =", frame_step)


# ==================================================
# COMPONENT A - TASK A1
# 2D LINE PLOT
# ==================================================

# Create x values from 1 to n_points
x = list(range(1, n_points + 1))

# Create y values = x squared
y = [value ** 2 for value in x]

# Check that the data is valid before plotting
if len(x) > 0 and len(x) == len(y):
    plt.figure(figsize=(8, 5))
    plt.plot(x, y)

    plt.title("Component A - 2D Line Plot")
    plt.xlabel("x")
    plt.ylabel("y = x^2")

    plt.grid(True)
    plt.show()
else:
    print("Error: x and y are not valid for plotting.")


# ==================================================
# COMPONENT A - TASK A2
# DISTRIBUTION PLOT
# ==================================================

# Create at least 30 repeated measurement values
data_values = [
    12, 13, 14, 15, 13, 14, 15, 16, 17, 14,
    13, 15, 16, 14, 12, 13, 15, 16, 17, 18,
    15, 14, 13, 16, 17, 15, 14, 12, 13, 15
]

# Print the first 10 values
print("\nFirst 10 values of data_values:")
print(data_values[:10])

# This graph helps us understand the distribution of repeated data
# because it shows which values happen most often and how spread out the data is.
plt.figure(figsize=(8, 5))
plt.hist(data_values, bins=8, edgecolor="black")

plt.title("Component A - Distribution Plot")
plt.xlabel("Measured Value")
plt.ylabel("Frequency")

plt.grid(True)
plt.show()


# ==================================================
# COMPONENT B - TASK B1
# PERSONALIZED 2D PLOT
# ==================================================

# Use the same x list and create y2
y2 = [k * value + shift for value in x]

# Print the first 5 pairs
print("\nFirst 5 (x, y2) pairs:")
for i in range(5):
    print((x[i], y2[i]))

# Plot x vs y2
plt.figure(figsize=(8, 5))
plt.plot(x, y2, marker="o", linestyle="--")

plt.title(f"Personalized 2D Plot - ID {student_id} - k={k}, shift={shift}")
plt.xlabel("x")
plt.ylabel("y2 = kx + shift")

plt.grid(True)
plt.show()


# ==================================================
# COMPONENT B - TASK B2
# PERSONALIZED 3D SCATTER PLOT
# ==================================================

# Create the 3 lists
x_3d = list(range(1, n_points + 1))
y_3d = [value + shift for value in x_3d]
z_3d = [k * value for value in x_3d]

# Print the first 5 points for debugging
print("\nFirst 5 (x, y, z) points:")
for i in range(5):
    print((x_3d[i], y_3d[i], z_3d[i]))

# Create the 3D scatter plot
fig = plt.figure(figsize=(8, 5))
ax = fig.add_subplot(111, projection="3d")

ax.scatter(x_3d, y_3d, z_3d)

ax.set_title(f"Personalized 3D Scatter Plot - ID {student_id}")
ax.set_xlabel("x")
ax.set_ylabel("y = x + shift")
ax.set_zlabel("z = kx")

plt.show()


# ==================================================
# COMPONENT B - TASK B3
# PERSONALIZED ANIMATION
# ==================================================

# Create x and y values for the animation
x_anim = list(range(0, n_points))
y_anim = [k * value + shift for value in x_anim]

# Create figure and axis
fig, ax = plt.subplots(figsize=(8, 5))
line, = ax.plot([], [], marker="o")

# Set axis limits
ax.set_xlim(0, n_points - 1)
ax.set_ylim(min(y_anim) - 1, max(y_anim) + 1)

ax.set_title(f"Animated Line Plot - ID {student_id}")
ax.set_xlabel("x")
ax.set_ylabel("y = kx + shift")
ax.grid(True)


# Initialize the line
def init():
    line.set_data([], [])
    return line,


# Update function for animation
def update(frame):
    print("Animating frame:", frame)

    current_x = x_anim[:frame + 1]
    current_y = y_anim[:frame + 1]

    line.set_data(current_x, current_y)
    return line,


# Frames increase by frame_step
frames_list = list(range(0, n_points, frame_step))

ani = FuncAnimation(
    fig,
    update,
    frames=frames_list,
    init_func=init,
    blit=True,
    repeat=False
)

plt.show()
