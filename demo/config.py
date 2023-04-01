import os
from spotipy.oauth2 import SpotifyOAuth
import spotipy

SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")
SPOTIFY_REDIRECT_URL = os.getenv("SPOTIFY_REDIRECT_URL")


def getSpotifyOb():
    # Set the access token scope
    scope = "user-read-playback-state,user-modify-playback-state"
    # Create a Spotipy object with the user's credentials
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIFY_CLIENT_ID,
                                                   client_secret=SPOTIFY_CLIENT_SECRET,
                                                   redirect_uri=SPOTIFY_REDIRECT_URL,
                                                   scope=scope))
    return sp


def setEnvVars():
    if os.path.exists(".env"):
        with open(".env") as env_file:
            for line in env_file:
                key, val = line.strip().split("=")
                os.environ[key] = val
