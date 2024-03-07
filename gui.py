import tkinter
import customtkinter
from main import get_token, search_for_artist, get_songs_by_artist

def runMain():
    token = get_token()
    artist_name = link.get()
    result = search_for_artist(token, artist_name)
    artistNameLabel.configure(text=result["name"])
    

    # will need to parse return or else it will be jibberish
    # get artist id
    artist_id = result["id"]
    songs = get_songs_by_artist(token, artist_id)
    str = ""
    for id, song in enumerate(songs):
        str += f"{id + 1}. {song['name']} \n"
    artistTopSong.configure(text=str)



# Designing system settings
# use users light/dark mode + default color theme
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("green")

# creating the frame
app = customtkinter.CTk()
app.geometry("720x480")
app.title("Search for Spotify Artist's Top Songs")

# Adding the UI elements
title = customtkinter.CTkLabel(app, text="Enter an artist's name")
title.pack(padx=10, pady=10)

# create user input
artist_name_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=artist_name_var)
link.pack()

# send button
send = customtkinter.CTkButton(app, text="send", command=runMain)
send.pack(padx=10, pady=10)

artistNameLabel = customtkinter.CTkLabel(app, text="")
artistNameLabel.pack()

artistTopSong = customtkinter.CTkLabel(app, text="")
artistTopSong.pack()

# use tkinter to send to main.py
# Run the app as a loop
app.mainloop()