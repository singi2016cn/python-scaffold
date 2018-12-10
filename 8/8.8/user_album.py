# 用户的专辑


def make_album(singer, album_name, song_number=0):
    album = {}
    album['singer'] = singer
    album['album_name'] = album_name
    if song_number > 0:
        album['song_number'] = song_number
    return album


q = '[输入\'q\'可以退出]'
while True:
    singer = input('请输入歌手名'+q+':\n')
    if singer == 'q':
        break
    album_name = input('请输入专辑名'+q+':\n')
    if album_name == 'q':
        break
    print('您的专辑信息是:\n')
    print(make_album(singer, album_name))

