# 检查用户名

current_users = ['singi', 'lily', 'admin', 'fangsi', 'xiaoling']
new_users = ['singi', 'wang', 'admin', 'liang', 'zhou']
for item in new_users:
    if item in current_users:
        print(item+',请输入别的名字')
    else:
        print(item+',该名称未被使用')


