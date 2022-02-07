def make_album(artist_name, album_title, num_songs = 0):
    if num_songs == None:
        album={"artist":artist_name,"title":album_title}
    else:
        album={"artist":artist_name,"title":album_title,"# of songs":num_songs}
    return album

print("Album 1:", make_album("Wierd Al Yankovic", "Running With Scissors", 12))
print("Album 2:", make_album("Wintergatan", "Wintergatan", 2))
print("Album 3:", make_album("John Denver", "Poems, Prayers & Promises", 12))
print("Album 4:", make_album("Natasha Tyrimos", "A Thousand Miles", 5))

print()
keepGoing = ""
album_num = 5
while keepGoing != "q":
    artist=input("Enter artist name: ")
    album=input("Enter album name: ")
    songs=int(input("Enter number of songs in the album: "))
    print(f"Album {album_num}:", make_album(artist, album, songs))
    keepGoing = input("Would you like to keep going? Enter \"q\" to quit: ")