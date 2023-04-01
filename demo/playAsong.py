from config import getSpotifyOb as sp


def playSong(song_name):
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
