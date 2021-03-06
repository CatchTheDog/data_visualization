import matplotlib.pyplot as plt

from random_walk import RandomWalk

# 模拟多次随机漫步
for value in range(0,10):
	rw = RandomWalk(50000)
	rw.fill_walk()
	
	# 设置绘图窗口的尺寸
	plt.figure(dpi=128,figsize=(10,6))
	point_numbers = list(range(rw.num_points))
	plt.scatter(rw.x_values,rw.y_values,c=point_numbers,cmap=plt.cm.Blues,edgecolors=None,s = 0.5)
	
	# 突出显示起点和终点
	plt.scatter(0,0,c='green',edgecolors=None,s=100)
	plt.scatter(rw.x_values[-1],rw.y_values[-1],c='red',edgecolors=None,s=100)
	
	# 隐藏坐标轴
	plt.axes().get_xaxis().set_visible(False)
	plt.axes().get_yaxis().set_visible(False)
	
	# plt.show()
	plt.savefig('./rw_img/rw_plot_'+ str(value) +'.png',bbox_inches='tight')
	
	# keep_running = input("Make another walk?(y/n):")
	# if keep_running == 'n':
	# 	break