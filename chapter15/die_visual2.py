from plotly.graph_objs import Bar, Layout
from plotly import offline
from die import Die

die = Die()

results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)

#print(results)

frequencies =[]
for value in range(1, die.num_sides+1):
    freq=results.count(value)
    frequencies.append(freq)
#     print(f"{value} {freq}")

# print(frequencies)

x_values=list(range(1, die.num_sides+1))
data=[Bar(x=x_values, y=frequencies)]
x_axis_config = {'title': 'Result'}
y_axis_config = {'title': 'Frequency of results'}
my_layout=Layout(title= 'Results of rolling dice', xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='d6.html')