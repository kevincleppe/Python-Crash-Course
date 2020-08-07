import matplotlib.pyplot as plt

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(2,4, s=200)

ax.set_title("Squares", fontsize=24)
ax.set_xlabel("Values", fontsize=14)
ax.set_ylabel("Squares of values", fontsize=14)

ax.tick_params(axis='both', which='major', labelsize=14)

plt.show()