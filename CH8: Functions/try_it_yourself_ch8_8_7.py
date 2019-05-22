def make_album(artist, album, numbers=''):
    """Return an artist name and an album title in a dictionary"""
    book = {
        'name_artist': artist.title(),
        'name_album': album.title()}
    if numbers:
        book['numbers'] = numbers
    return book

merge = make_album('michael jackson', 'invincible', numbers=22)
print(merge)

merge = make_album('justin timberlake', '20-20 experience', numbers=14)
print(merge)

merge = make_album('frank ocean', 'blonde', numbers=7)
print(merge)