# 宠物

pet1 = {'xiaohei': {
    'type': 'dog',
    'master': 'singi'
}}
pet2 = {'xiaobai': {
    'type': 'cat',
    'master': 'shuting'
}}
pets = [pet1, pet2]
for pet in pets:
    for k, v in pet.items():
        print('pet name is ' + k)
        print('pet type is ' + v['type'])
        print('pet master is ' + v['master'])
