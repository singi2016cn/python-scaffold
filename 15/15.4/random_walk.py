"""在类 RandomWalk 中，x_step 和 y_step 是根据相同的条件生
成的：从列表[1, -1]中随机地选择方向，并从列表[0, 1, 2, 3, 4]中随机地选择距离。
请修改这些列表中的值，看看对随机漫步路径有何影响。尝试使用更长的距离选择列表，
如 0~8；或者将1 从 x 或 y 方向列表中删除"""


import matplotlib.pyplot as plt
from random import choice


class RandomWalk:
    """一个生成随机漫步数据的类"""

    def __init__(self, num_points=5000):
        """初始化随机漫步的属性"""
        self.num_points = num_points

        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """计算随机漫步包含的所有点"""

        # 不断漫步，直到列表达到指定的长度
        while len(self.x_values) < self.num_points:
            # 决定前进方向以及沿这个方向前进的距离
            x_direction = choice([1, -1])
            x_distance = choice([0, 1, 2, 3, 4, 5, 6, 7, 8])
            x_step = x_direction * x_distance

            y_direction = choice([1, 0])
            y_distance = choice([0, 1, 2])

            y_step = y_direction * y_distance

            # 拒绝原地踏步
            if x_step == 0 and y_step == 0:
                continue

            # 计算下一个点的x和y值
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)
