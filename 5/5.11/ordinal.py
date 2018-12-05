# 序数

ordinal = list(range(1, 10))
for item in ordinal:
    if item == 1:
        print(str(item)+'st')
    elif item == 2:
        print(str(item)+'nd')
    elif item == 3:
        print(str(item)+'rd')
    else:
        print(str(item)+'th')



