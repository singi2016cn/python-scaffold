# 票价

active = True

while active:
    age = input('\n请输入您的年龄:\n')
    if age == 'q':
        print('输入结束')
        active = False
        break
    age = int(age)
    if age < 3:
        print('您不需要买票')
    elif age >= 3 and age < 12:
        print('您的票价是:10$')
    else:
        print('您的票价是:15$')

