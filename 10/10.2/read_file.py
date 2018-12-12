"""读取文件"""

with open('learning_python.txt') as file_object:
    lines = file_object.readlines()

for item in lines:
    print(item.replace('Python', 'C').rstrip())

