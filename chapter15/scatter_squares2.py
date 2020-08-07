import matplotlib.pyplot as plt


x_values=range(1, 1001)
y_values=[x**2 for x in x_values]

plt.style.use('seaborn')
fix, ax = plt.subplots()
ax.set_title("Squares", fontsize=24)
ax.set_xlabel("Values", fontsize=14)
ax.set_ylabel("Squares of values", fontsize=14)
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Purples, s =10)
ax.axis([0, 1100, 0, 1100000])

plt.show()