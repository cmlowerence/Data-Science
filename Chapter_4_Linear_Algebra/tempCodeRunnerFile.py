import matplotlib.pyplot as plt
import numpy as np

# Define two vectors
vector1 = np.array([2, 3])
vector2 = np.array([-1, 2])

# Calculate the vector sum
vector_sum = vector1 + vector2

# Create a figure and axis
fig, ax = plt.subplots()

# Plot the vectors
ax.quiver(0, 0, vector1[0], vector1[1], angles='xy', scale_units='xy', scale=1, color='blue', label='Vector 1')
ax.quiver(0, 0, vector2[0], vector2[1], angles='xy', scale_units='xy', scale=1, color='red', label='Vector 2')
ax.quiver(0, 0, vector_sum[0], vector_sum[1], angles='xy', scale_units='xy', scale=1, color='green', label='Vector Sum')

# Set the aspect ratio of the plot to be equal
ax.set_aspect('equal')

# Set labels for x and y axes
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# Set the limits of the plot
plt.xlim(-2, 4)
plt.ylim(-1, 5)

# Add a legend
plt.legend()

# Show the plot
plt.grid(True)
plt.show()
