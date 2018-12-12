"""写入文件"""

file_name = 'user_input.txt'
user_input = input('请输入您要存储的信息:\n')
with open(file_name, 'w',encoding='utf8') as file_object:
    file_object.write(user_input)
    print('写入成功')


