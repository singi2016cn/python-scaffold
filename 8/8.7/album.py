# 专辑


def make_album(singer, album_name, song_number=0):
    album = {}
    album['singer'] = singer
    album['album_name'] = album_name
    if song_number > 0:
        album['song_number'] = song_number
    return album

print(make_album('beijing', 'singi'))
print(make_album('shenzhen', 'sunjun'))
print(make_album('tokyo', 'xiaoling'))
print(make_album('tokyo', 'xiaoling', 8))
