def make_album(artist, album):
    music={'artist':  artist.title(), 'album': album.title()}
    return music

music = make_album('alicia myers', 'back to back')
print(music)