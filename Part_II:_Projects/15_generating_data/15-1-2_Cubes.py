#!/usr/bin/env python3

# 15-1. Cubes: A number raised to the third power is a cube. Plot the first five
# cubic numbers, and then plot the first 5,000 cubic numbers.
# 15-2. Colored Cubes: Apply a colormap to your cubes plot


from matplotlib import pyplot as plt

plt.style.use("seaborn-v0_8")

# input_values = [1, 2, 3, 4, 5]
# cubes = [1, 8, 27, 64, 125]


x_values = range(1, 5001)
y_values = [x**3 for x in x_values]

fig, ax = plt.subplots()

# ax.plot(input_values, cubes, linewidth=3)
# apply colormap to the cubes

ax.axis([0, 5100, 0, 5100**3])
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)


plt.show()
