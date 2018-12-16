"""方法 fill_walk()很长。请新建一个名为 get_step()的方法，用于确定
每次漫步的距离和方向，并计算这次漫步将如何移动。然后，在 fill_walk()中调用
get_step()两次：
x_step = get_step()
y_step = get_step()
通过这样的重构，可缩小 fill_walk()的规模，让这个方法阅读和理解起来更容易"""


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

            x_step = self.get_step()
            y_step = self.get_step()

            # 拒绝原地踏步
            if x_step == 0 and y_step == 0:
                continue

            # 计算下一个点的x和y值
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)

    def get_step(self, direction_start=1, direction_end=-1, distance_start=0, distance_end=5):
        """获取x,y周轴每次走的位置"""
        direction = choice([direction_start, direction_end])
        distance = choice(list(range(distance_start, distance_end)))
        return direction * distance

