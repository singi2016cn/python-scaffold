# 你的比萨和我的比萨

pizzas = ['shuiguo', 'kaorou', 'bingqiling']

for pizza in pizzas:
    print('I love '+pizza+' pizza.')
print('I really love pizza!')

friend_pizzas = pizzas[:]
pizzas.append('haoyou')
friend_pizzas.append('regou')
print('My favorite pizzas are:')
for pizza in pizzas:
    print(pizza)
print('My friend’s favorite pizzas are:')
for pizza in friend_pizzas:
    print(pizza)
