"""编程语言调查"""

import os


print('输入\'q\'结束\n')
file_name = 'programming_investigate_log.txt'

while True:
    programming = input('请输入您的编程语言:\n')
    if programming == 'q':
        break

    if os.path.exists(file_name):
        write_model = 'a'
    else:
        write_model = 'w'

    with open(file_name, write_model, encoding='utf8') as file_object:
        file_object.write(programming+'\n')


