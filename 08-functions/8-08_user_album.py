# 8-8. User Albums: Start with your program from Exercise 8-7. Write a while
# loop that allows users to enter an album’s artist and title. Once you have that
# information, call make_album() with the user’s input and print the dictionary
# that’s created. Be sure to include a quit value in the while loop.


def make_album(artist: str, title: str, songs: int = 0) -> dict:
    album = {"artist": artist.title(), "title": title.title()}
    if songs:
        album["songs"] = songs
    return album


while True:
    in_artist = input("Artist (quit to quit): ")
    if in_artist == "quit":
        break
    in_title = input("Title: ")
    in_songs = input("Number of songs: ")
    if in_songs:
        in_songs = int(in_songs)
    else:
        in_songs = 0
    print(make_album(artist=in_artist, title=in_title, songs=in_songs))
