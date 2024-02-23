#!/usr/bin/env python3
import matplotlib.pyplot as plt

plt.style.use("seaborn-v0_8")
# x_values = [1, 2, 3, 4, 5]
# y_values = [1, 4, 9, 16, 25]
x_values = range(1, 1001)
y_values = [x**2 for x in x_values]


fig, ax = plt.subplots()


# ax.scatter(x_values, y_values,color='red', s=10)
# ax.scatter(x_values, y_values, color=(0, 0.8, 0), s=10)
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)


# Set Chart Title and Label axes
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Set size of tick labels
ax.tick_params(labelsize=14)

# Set the range for each axis
ax.axis([0, 1100, 0, 1_100_000])
ax.ticklabel_format(style="plain")

plt.show()
# plt.savefig("squares_plot.png", bbox_inches="tight")
