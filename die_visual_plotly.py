import plotly.express as px

from die import Die
# Create two D8 dice.
die_1 = Die(3)
die_2 = Die(3)

# Make some rolls, and store results in a list by using for loop.
# results = []
# for roll_num in range(100_000):
#     result = die_1.roll() * die_2.roll()
#     results.append(result)

# Make some rolls, and store results in a list by using list comprehension.
results = [die_1.roll() * die_2.roll() for i in range(1_000)]

# Analyze the results by using for loop.
# frequencies = []
# max_result = die_1.num_sides * die_2.num_sides
# poss_results = range(1, max_result+1)
# for value in poss_results:
#     frequency = results.count(value)
#     frequencies.append(frequency)

# Analyze the results by using list comprehension.
max_result = die_1.num_sides * die_2.num_sides
poss_results = range(1, max_result+1)
frequencies = [results.count(value) for value in poss_results]

# Visualize the results.
title = "Results of Rolling two D8 Die"
labels = {'x': 'Result', 'y': 'Frequency of Result'}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)

# Further customize chart.
fig.update_layout(xaxis_dtick=1)

# fig.write_html('dice_visual_d6d10.html')
fig.show()