#!/usr/bin/env python3

# TRY IT YOURSELF
# 15-3. Molecular Motion: Modify rw_visual.py by replacing ax.scatter() with
# ax.plot(). To simulate the path of a pollen grain on the surface of a drop of
# water, pass in the rw.x_values and rw.y_values, and include a linewidth argu-
# ment. Use 5,000 instead of 50,000 points to keep the plot from being too bu

import matplotlib.pyplot as plt
from random_walk import RandomWalk


# Make a random walk.
rw = RandomWalk(5000)
rw.fill_walk()

# Plot the points in the walk.
plt.style.use("classic")
fig, ax = plt.subplots()
ax.plot(rw.x_values, rw.y_values, linewidth=3)
ax.set_aspect("equal")

# Remove the axes
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)

plt.show()
