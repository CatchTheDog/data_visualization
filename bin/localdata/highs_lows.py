import csv
from datetime import datetime

from matplotlib import pyplot as plt

# 从文件中获取最高气温
filename = 'sitka_weather_07-2014.csv'
with open(filename) as f:
	reader = csv.reader(f)
	header_row = next(reader)
	
	# for index, column_header in enumerate(header_row):
	# 	print(index,column_header)
	
	dates, highs = [], []
	for row in reader:
		current_date = datetime.strptime(row[0], "%Y-%m-%d")
		dates.append(current_date)
		highs.append(int(row[1]))
	
	# 根据获取的数据绘制图形
	fig = plt.figure(dpi=128, figsize=(10, 6))
	plt.plot(dates, highs, c='red')
	
	# 设置图形的格式
	plt.title('Daliy high temperatures, July 2014', fontsize=24)
	plt.xlabel('', fontsize=16)
	
	# x 轴时间自适应显示，避免重叠
	fig.autofmt_xdate()
	plt.ylabel("Temperature(F)", fontsize=16)
	plt.tick_params(axis='both', which='major', labelsize=16)
	
	plt.show()
