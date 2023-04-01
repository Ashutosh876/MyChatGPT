import spotipy
from spotipy.oauth2 import SpotifyOAuth


def playSong(song_name):
    # Set the access token scope
    scope = "user-read-playback-state,user-modify-playback-state"
    # Create a Spotipy object with the user's credentials
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id='3124ea57e47e4c7cbccd63173c5cfe42',
                                                   client_secret='fd4a56c1512d484cb5b0dbe7333b977a',
                                                   redirect_uri='http://localhost:8080',
                                                   scope=scope))
    # Get the song name from the user
    # song_name = input("Enter the name of the song you want to play: ")
    # Search for the song
    results = sp.search(q=song_name, type="track", limit=1)
    # Extract the track URI from the search results
    if len(results["tracks"]["items"]) > 0:
        track_uri = results["tracks"]["items"][0]["uri"]
        print(f"Track URI for '{song_name}': {track_uri}")
    else:
        print(f"No song found with the name '{song_name}'.")
    # Play the song using the track URI
    if track_uri:
        sp.start_playback(uris=[track_uri])
        print(f"Playing '{song_name}'.")
