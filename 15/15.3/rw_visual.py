import matplotlib.pyplot as plt
from random_walk import RandomWalk


# 创建一个RandomWalk实例，并将其包含的点都绘制出来
while True:
    rw = RandomWalk(50000)
    rw.fill_walk()
    point_numbers = list(range(rw.num_points))
    plt.plot(rw.x_values, rw.y_values, linewidth=1)
    # 突出起点和终点
    plt.plot(0, 0)
    plt.plot(rw.x_values[-1], rw.y_values[-1])

    # 隐藏坐标轴
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)

    # 设置绘图窗口的尺寸
    plt.figure(dpi=128, figsize=(10, 6))

    plt.show()

    keep_running = input('继续生成下一个随机图吗?(y/n)')
    if keep_running == 'n':
        break

