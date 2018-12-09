# 10的整数倍

number = input('请问需要测试的数字是？\n')
number = int(number)
if (number % 10) == 0:
    print('是10的整数倍')
else:
    print('不是10的整数倍')
