# 以特殊方式跟管理员打招呼

users = ['singi', 'lily', 'admin', 'fangsi', 'xiaoling']
for item in users:
    if item == 'admin':
        print('Hello admin, would you;like to see a status report?')
    else:
        print('Hello '+item+', thank you for logging in again')

