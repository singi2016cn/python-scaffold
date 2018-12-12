"""访客名单"""

import os


print('输入\'q\'结束\n')
file_name = 'user_great_log.txt'

while True:
    username = input('请输入您的姓名:\n')
    if username == 'q':
        break
    great = '欢迎:'+username+'\n'
    print(great)

    if os.path.exists(file_name):
        write_model = 'a'
    else:
        write_model = 'w'

    with open(file_name, write_model, encoding='utf8') as file_object:
        file_object.write(great)


