# music_playlist={"Hangman":{"artists":"Dave", "genere": "hipop"},    
#                 "starboy":{"artists":"Weekend" ,"genere":"hipop"},
#                 "jealous":{"artists":"Labrinth","genere": "Pop"}}
# print(music_playlist)
# def add_song(title,artists,genere):
#     if title in music_playlist:
#         print(f"The song '{title}' already exists in the playlist.")
#     else:
#         music_playlist[title] = {"artist": artists, "genre": genere}
#         print(f"Added '{title}' by {artists} to the playlist.")
        
# # Test the function
# add_song("Yesterday", "The Beatles", "Rock")
# add_song("Bohemian Rhapsody", "Queen", "Rock")

# # Print the updated playlist to verify
# print(music_playlist)        
# Define the initial playlist dictionary
# Formatting Variables




format_output = "\033[47m\033[30m"
format_reset = "\033[0m"
# Formatted Message - Signify Start of Output
print(f"{format_output}---START---{format_reset}")
playlist = {
    "Bohemian Rhapsody": {"artist": "Queen", "genre": "Rock"},
    "Billie Jean": {"artist": "Michael Jackson", "genre": "Pop"},
    "Hotel California": {"artist": "Eagles", "genre": "Rock"},
    "Shape of You": {"artist": "Ed Sheeran", "genre": "Pop"},
    "Blinding Lights": {"artist": "The Weeknd", "genre": "R&B"},
    "Rolling in the Deep": {"artist": "Adele", "genre": "Pop"},
    "Smells Like Teen Spirit": {"artist": "Nirvana", "genre": "Grunge"},
    "Imagine": {"artist": "John Lennon", "genre": "Rock"},
    "Uptown Funk": {"artist": "Mark Ronson ft. Bruno Mars", "genre": "Funk"},
    "Shallow": {"artist": "Lady Gaga & Bradley Cooper", "genre": "Pop"},
}

# Define the add_song function
def add_song(title, artist, genre):
    if title in playlist:
        print(f"The song '{title}' already exists in the playlist.")
    else:
        playlist[title] = {"artist": artist, "genre": genre}
        print(f"Added '{title}' by {artist} to the playlist.")

# Test the function
add_song("Yesterday", "The Beatles", "Rock")
add_song("Bohemian Rhapsody", "Queen", "Rock")

# Print the updated playlist to verify
def view_playlist():
    if not playlist:
        print("The playlist is empty.")
    else:
        for title, details in playlist.items():
            print(f"Title: {title}")

# Test the view_playlist function
view_playlist()
def update_playlist(title,genre,artist):
    if playlist:
        print("the playlist has not been changed")
    else:
        print("playlist has been updated")
print(update_playlist)

def delete_song(title):
    if title in playlist:
        del playlist[title]
        print(f"The song '{title}' has been removed from the playlist.")
    else:
        print(f"The song '{title}' does not exist in the playlist.")
















# Test the delete_song function
delete_song("Bohemian Rhapsody")
delete_song("Nonexistent Song")











































# View the updated playlist
view_playlist()



































# Formatted Message - Signify End of Output
print(f"{format_output}---END---{format_reset}")