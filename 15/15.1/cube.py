"""立方:
数字的三次方被称为其立方。
请绘制一个图形，显示前 5 个整数的立方值，再绘制一个图形，显示前 5000 个整数的立方值"""


import matplotlib.pyplot as plt

numbers = list(range(1, 6))
values = [v**3 for v in range(1, 6)]
plt.plot(numbers, values)
plt.title('前 5 个整数的立方值', fontproperties="SimHei")
plt.xlabel('数字', fontproperties="SimHei")
plt.ylabel('值', fontproperties="SimHei")
plt.show()


numbers2 = list(range(1, 5001))
values2 = [v**3 for v in range(1, 5001)]
plt.plot(numbers2, values2)
plt.title('前 5000 个整数的立方值', fontproperties="SimHei")
plt.xlabel('数字', fontproperties="SimHei")
plt.ylabel('值', fontproperties="SimHei")
plt.show()

