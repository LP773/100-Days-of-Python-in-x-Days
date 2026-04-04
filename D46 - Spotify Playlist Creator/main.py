from bs4 import BeautifulSoup
import requests
import os
import json
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Spotify Authentication
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    scope="playlist-modify-private",
    redirect_uri="https://example.org/callback",
    client_id=os.getenv("CLIENT_ID"),
    client_secret=os.getenv("CLIENT_SECRET"),
    show_dialog=True,
    cache_path="./D46/token.txt"
    )
)
user_id = sp.current_user()["id"]

input_date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:149.0) Gecko/20100101 Firefox/149.0"
}

billboard_request = requests.get(f"https://www.billboard.com/charts/hot-100/{input_date}/", headers=header)
soup = BeautifulSoup(billboard_request.content, "html.parser")
chart_container = soup.find_all(name="li", class_="a-chart-result-item-container")

# list_of_songs = []
# list_of_artists = []
song_and_artist = []

# List of Songs
for containers in chart_container:
    # Grabbing Song
    song_name = containers.find_all(name="h3", class_="c-title")
    #list_of_songs.append(song_name[0].text.strip())
    # Grabbing Artist
    artist_name = containers.find_all(name="span", class_="c-label")
    #list_of_artists.append(artist_name[0].text.strip())
    song_and_artist.append({
        "song":song_name[0].text.strip(),
        "artist": artist_name[0].text.strip()
    })

# Write songs to local file
# with open("./D46/songs.json", "w") as song_output:
#     json.dump(song_and_artist, song_output, indent=4)

# List of Spotify URLs

# Load local songs file
# with open("./D46/songs.json", "r") as song_input:
#     song_data = json.load(song_input)

song_uris = []
for song in song_and_artist:
    result = sp.search(q=f"track:{song["song"]} artist:{song["artist"]}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song['song']} by {song['artist']} not found. Skipped")

# Write URIs to file
# with open("./D46/song_uris.txt", "w") as uri_output:
#     for uri in song_uri:
#         uri_file.write(uri + "\n")

# Read local URL file
# with open("./D46/song_uris.txt", "r") as uri_input:
#     song_uris = uri_input.read().splitlines()

# Create Playlist
playlist_name = f"{input_date} Billboard 100"
playlist = sp.current_user_playlist_create(name=playlist_name, public=False)
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
print("Playlist created successfully")