import pygal
from die import Die


# 创建2个D6
die = Die()
die2 = Die()
die3 = Die()

# 掷几次骰子，并将结果存储在一个列表中
results = []
for roll_num in range(1000):
    result = die.roll() + die2.roll() + die3.roll()
    results.append(result)

# 分析结果
frequencies = []
max_result = die.num_sides + die2.num_sides + die3.num_sides
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# 对结果进行可视化
hist = pygal.Bar()

hist.title = '3个6面骰子投掷1000次的概率分布'
hist.x_labels = list(range(2, die.num_sides+die2.num_sides+1))
hist.x_title = '结果'
hist.y_title = '次数'

hist.add('D6 + D6 + D6', frequencies)
hist.render_to_file('die_visual.svg')
