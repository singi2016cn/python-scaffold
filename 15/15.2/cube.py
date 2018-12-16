"""彩色立方：给你前面绘制的立方图指定颜色映射"""


import matplotlib.pyplot as plt


numbers = list(range(1, 1001))
values = [v**3 for v in range(1, 1001)]
plt.scatter(numbers, values, c=values, cmap=plt.cm.Greens, edgecolor='none')
plt.title('前 1000 个整数的立方值', fontproperties="SimHei")
plt.xlabel('数字', fontproperties="SimHei")
plt.ylabel('值', fontproperties="SimHei")
plt.show()

