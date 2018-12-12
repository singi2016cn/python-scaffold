"""沉默的猫和狗"""

cats_file = 'cats.txt'
try:
    with open(cats_file) as f:
        cats = f.readlines()
        print(cats)
except FileNotFoundError:
    pass

dogs_file = 'dogs.txt'
try:
    with open(dogs_file) as f:
        dogs = f.readlines()
    print(dogs)
except FileNotFoundError:
    print(dogs_file+'该文件不存在')
