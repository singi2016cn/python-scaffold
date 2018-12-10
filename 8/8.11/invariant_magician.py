# 不变的魔术师


def show_magicians(magicians):
    for magician in magicians:
        print('magician\'s name is ' + magician)


def make_great(magicians):
    for item in magicians:
        magicians[magicians.index(item)] = 'The Great ' + item
    return magicians


magicians = ['singi', 'sunjun']
magicians2 = make_great(magicians[:])
show_magicians(magicians)
show_magicians(magicians2)
