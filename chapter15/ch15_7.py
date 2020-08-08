from plotly.graph_objs import Bar, Layout
from plotly import offline
from die import Die

die1 = Die()
die2 = Die()
die3 = Die()
results = []
for roll_num in range(100000):
    result = die1.roll() + die2.roll() + die3.roll()
    results.append(result)

#print(results)

frequencies =[]
max_results= die1.num_sides +die2.num_sides + die3.num_sides
for value in range(3, max_results+1):
    freq=results.count(value)
    frequencies.append(freq)
#     print(f"{value} {freq}")

# print(frequencies)

x_values=list(range(3, max_results+1))
data=[Bar(x=x_values, y=frequencies)]
x_axis_config = {'title': 'Result', 'dtick': 1}
y_axis_config = {'title': 'Frequency of results'}
my_layout=Layout(title= 'Results of rolling dice', xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='d6.html')