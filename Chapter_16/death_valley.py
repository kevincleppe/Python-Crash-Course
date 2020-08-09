import csv
import csv
import matplotlib.pyplot as plt
from datetime import datetime

filename= 'data/highland.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    # print(header_row)
    
    # for index, column_header in enumerate(header_row):
    #     print(index, column_header)
    dates, highs, lows=[], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        try:
            high = int(row[4])
            low = int(row[5])
        except ValueError:
            print(f"Missing date {current_date}")
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

plt.style.use('seaborn')
fig, ax = plt.subplots()

ax.plot(dates, highs, c='red')
ax.plot(dates, lows, c='green')
plt.fill_between(dates, lows, highs, facecolor='blue', alpha=0.1)
plt.title("Daily highs and lows temprature, July 2018", fontsize =24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temp (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)
plt.show()
# print(highs)
