import csv
from datetime import datetime

from matplotlib import pyplot as plt

# 从文件中读取数据
filename = "sitka_weather_2014.csv"
with open(filename) as f:
	reader = csv.reader(f)
	header_row = next(reader)
	
	dates, highs, lows = [], [], []
	
	for row in reader:
		current_date = datetime.strptime(row[0], '%Y-%m-%d')
		dates.append(current_date)
		highs.append(int(row[1]))
		lows.append(int(row[3]))

# 绘制图片

fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, c='red')
plt.plot(dates, lows, c='blue')

# 给最高气温和最低气温中间区域着色
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

plt.xlabel('', fontsize=16)
plt.ylabel('Temperature(F)', fontsize=16)
plt.title("Daily high and low temperatures - 2014")
plt.tick_params(axis='both', which='major', labelsize=16)
fig.autofmt_xdate()

plt.show()
