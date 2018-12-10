# 魔术师


def show_magicians(magicians):
    for magician in magicians:
        print('magician\'s name is ' + magician)



def make_great(magicians):
    i = 0
    for item in magicians:
        magicians[i] = 'The Great ' + item
        i = i + 1


magicians = ['singi', 'sunjun']
make_great(magicians)
show_magicians(magicians)
