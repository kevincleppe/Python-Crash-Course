import matplotlib.pyplot as plt
filename = "scores.txt"
game_scores = []
with open(filename) as file_object:
    for line in file_object:
        game_scores.append(float(line))
    print(game_scores)
"numbers are being appended as strings, need to convert to ints"

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(game_scores, linewidth=3)


plt.show()
