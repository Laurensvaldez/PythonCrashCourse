# Start with your program from exercise 8-7. Write a while loop that allows users to enter an album's artist and title.
# Once you have that information, call make_album() with the user's input and print the dictionary that's created.
# Be sure to include a quit value in the while loop.

def make_album(artist, title, tracks=0):
    """Return an artist name and an album title in a dictionary"""
    book = {
        'name_artist': artist.title(),
        'name_album': title.title()}
    if tracks:
        book['tracks'] = tracks
    return book

# prepare the prompts.
title_prompt = "\nWhat album are you thinking of? "
artist_prompt = "Who's the artist? "

# Let the user know how to quit.
print("Enter 'quit' at any time to stop.")

while True:
    title = input(title_prompt)
    if title == 'quit':
        break

    artist = input(artist_prompt)
    if artist == 'quit':
        break

    album = make_album(artist, title)
    print(album)

print("\nThanks for responding!")