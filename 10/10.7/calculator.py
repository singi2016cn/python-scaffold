"""加法运算"""

print('输入\'q\'结束\n')

while True:
    try:
        num1 = int(input('请输入第1个数字:\n'))
        break
    except ValueError:
        print('请输入数字')

while True:
    try:
        num2 = int(input('请输入第2个数字:\n'))
        break
    except ValueError:
        print('请输入数字')

num_sum = num1 + num2
print('结果是:' + str(num_sum))

