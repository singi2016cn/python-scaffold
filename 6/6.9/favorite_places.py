# 喜欢的地方

favorite_places = {
    'singi': ['guilin', 'zhanjiang', 'guangxi'],
    'shuting': ['zhanjiang', 'guangdong', 'shenzhen']
}

for k, v in favorite_places.items():
    for item in v:
        print('favorite places of ' + k + ' is ' + item)
