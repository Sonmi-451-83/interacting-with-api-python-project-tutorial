import os
import pandas as pd
import seaborn as sns
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# load the .env file variables
load_dotenv()

client_id = os.environ.get("CLIENT_ID")
client_secret = os.environ.get("CLIENT_SECRET")

my_api = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id = client_id,client_secret = client_secret))

results = my_api.artist_top_tracks(artist_id="06HL4z0CvFAxyc27GXpf02")

taylor_dict = {"name": [track['name'] for track in results['tracks'][:10]], "popularity": [track['popularity'] for track in results['tracks'][:10]], "duration_ms": [track['duration_ms'] for track in results['tracks'][:10]]}

df = pd.DataFrame.from_dict(taylor_dict)

top_3 = df.sort_values(by='popularity')[0:3]

print(top_3)

sns.scatterplot(data=df, x="duration_ms", y="popularity")

#Se puede observar que no hay relacción entre la duración del track y su popularidad