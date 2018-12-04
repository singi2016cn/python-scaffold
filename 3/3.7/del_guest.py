# 删除嘉宾

names = []
names.append('singi')
names.append('lily')
names.append('sam')

names.insert(0, 'xiaoling')
names.insert(2, 'fangsi')
names.append('zhangqing')

print('I can only invite two guest for dinner.')

guest = names.pop()
print(guest+',I\'m sorry,I can\'t invite you for dinner.')
guest = names.pop()
print(guest+',I\'m sorry,I can\'t invite you for dinner.')
guest = names.pop()
print(guest+',I\'m sorry,I can\'t invite you for dinner.')
guest = names.pop()
print(guest+',I\'m sorry,I can\'t invite you for dinner.')

greets = ',would you like to have dinner with me ?'
print(names[0]+greets)
print(names[1]+greets)
del names[0]
del names[0]
print(names)
