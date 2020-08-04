import matplotlib.pyplot as plt
# 
game_scores = []
# with open(filename) as file_object:
#     for i in range(filename):
#         i=int(i)
#         print(i)
#     # for line in file_object:
#     #     game_scores.append(line)
#     # print(game_scores)

# for i in range(0, len(game_scores)):
#     game_scores[i] = int(game_scores[i])

# print(game_scores)

"numbers are being appended as strings, need to convert to ints"
filename = "/Users/kev/Desktop/python/Python-Crash-Course/scores.txt"
with open(filename, 'r') as f:
    lines = f.readlines()
    x = [int(line.split()[0]) for line in lines]
    y = [int(line.split()[1]) for line in lines]
plt.plot(x ,y)
plt.show()

# plt.style.use('seaborn')
# fig, ax = plt.subplots()
# ax.plot(game_scores, linewidth=3)
# plt.show()
