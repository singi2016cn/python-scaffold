# 五香烟熏牛肉卖完了

sandwich_orders = ['singi', 'shuting', 'pastrami', 'pastrami', 'pastrami', 'pastrami']
finished_sandwitch = []

print('pastrami all sold out.')
pastrami_is_sold_out = True
while pastrami_is_sold_out:
    if 'pastrami' in sandwich_orders:
        sandwich_orders.remove('pastrami')
    else:
        break

for item in sandwich_orders:
    print('I made your '+item+' sandwitch.')
    finished_sandwitch.append(item)
print('all sandwitch finished.there are:')
print(finished_sandwitch)
