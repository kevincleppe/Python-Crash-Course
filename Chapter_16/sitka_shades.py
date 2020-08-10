import csv
import matplotlib.pyplot as plt
from datetime import datetime

filename = 'data/sitka2.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    # print(header_row)
    
    # for index, column_header in enumerate(header_row):
    #     print(index, column_header)
    dates, highs, lows=[], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        high = int(row[5])
        low = int(row[6])
        dates.append(current_date)
        highs.append(high)
        lows.append(low)

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha =0.5)
ax.plot(dates, lows, c='green', alpha =0.5)
plt.fill_between(dates, lows, highs, facecolor='blue', alpha=0.1)
plt.title("Daily highs and lows temprature, July 2018", fontsize =24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temp (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)
plt.show()
# print(highs)
