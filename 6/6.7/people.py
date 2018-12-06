# 人

people1 = {'first_name': 'qin', 'last_name': 'yi', 'age': 26, 'city': 'shenzhen'}
people2 = {'first_name': 'sun', 'last_name': 'jun', 'age': 28, 'city': 'shenzhen'}
people3 = {'first_name': 'xiao', 'last_name': 'ling', 'age': 24, 'city': 'shenzhen'}
people = [people1, people2, people3]
for item in people:
    for k, v in item.items():
        print(k + ':' + str(v))
