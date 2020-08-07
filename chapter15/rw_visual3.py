import matplotlib.pyplot as plt

from random_walk import Randomwalk
while True:
    rw = Randomwalk()
    rw.fill_walk()
    rw=Randomwalk(50_000)
    plt.style.use('classic')
    fig, ax = plt.subplots()
    point_numbers =range(rw.num_points)
    #ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Purples, s =10)
    #ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Reds, s=15)
    #ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, linewidth=1)

    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    # ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none', s=15)
    # ax.scatter(0,0, c='green', edgecolors='none', s=100)
    # ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none', s=1)
    fix, ax = plt.subplots(figsize=(15,9))
    plt.show()
    keep_running = input("Make another walk?")
    if keep_running == 'n':
        break