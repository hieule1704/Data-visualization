import matplotlib.pyplot as plt

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
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(poss_results, frequencies, linewidth=3)

# Set chart title and label axes.
ax.set_title('Results of Rolling two D3 Die', fontsize=24)
ax.set_xlabel('Result', fontsize=14)
ax.set_ylabel('Frequency of Result', fontsize=14)

# Set size of tick labels.
ax.tick_params(labelsize=14)

plt.show()