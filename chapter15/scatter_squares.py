import matplotlib.pyplot as plt

x=[1,2,3,4,5]
y=[1,4,9,16,25]

plt.style.use('seaborn')
fix,  ax = plt.subplots()
ax.scatter(x,y, s=100)

plt.show()