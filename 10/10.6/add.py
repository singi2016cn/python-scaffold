"""加法运算"""

print('输入\'q\'结束\n')

num1 = input('请输入第1个数字:\n')
num2 = input('请输入第2个数字:\n')

try:
    num_sum = int(num1) + int(num2)
except ValueError:
    print('请输入数字')
else:
    print('结果是:' + str(num_sum))

