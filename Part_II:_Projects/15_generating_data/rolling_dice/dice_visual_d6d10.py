#!/usr/bin/env python3

# 5-9. Die Comprehensions: For clarity, the listings in this section use the long
# form of for loops. If you’re comfortable using list comprehensions, try writing a
# comprehension for one or both of the loops in each of these program


import plotly.express as px

from die import Die

# Create two D6 dice..

die1 = Die()
die2 = Die(10)

# Make some rolls, and store results in a list.

# use list comprehension to fill the results

results = [die1.roll() + die2.roll() for _ in range(50_000)]

# results = []
# for roll_num in range(50_000):
#     result = die1.roll() + die2.roll()
#     results.append(result)


# Analyze the results.

# use list comprehension to fill the frequencies

max_result = die1.num_sides + die2.num_sides
poss_results = range(2, max_result + 1)
frequencies = [
    results.count(value) for value in range(2, die1.num_sides + die2.num_sides + 1)
]
# frequencies = []

# for value in poss_results:
#     frequency = results.count(value)
#     frequencies.append(frequency)

# Visualize the results
title = "Results of Rolling Two D10 50,000 times."
labels = {"x": "Result", "y": "Frequency of Result"}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)

# Further customize the chart
fig.update_layout(xaxis_dtick=1)
fig.write_html("dice_visual_d6d10.html")
fig.show()
