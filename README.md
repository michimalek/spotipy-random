# Spotipy-random

## Description

This package extends the already existing [spotipy](https://spotipy.readthedocs.io/en/2.19.0/) API client library with a randomized search functionallity. Both libraries are based on the official [Spotify API](https://developer.spotify.com/documentation/).

## Installation

This package can be installed through pip with the following command:

```
pip install spotipy-random
```

The spotipy package is also required and can be installed with:

```
pip install spotipy
```

## Usage

To use this library first create a new spotipy client object including your personal Spotify API client_id and client_secret. Then the `get_random` method can be used to search for random tracks, albums and more. You can also specify search filters, although some filter will not work with each search type (Check details in the [Spotify API documentation](https://developer.spotify.com/documentation/web-api/reference/#/operations/search)).

```py
from spotipy import Spotfiy
from spotipy_random import get_random

spotify_client = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
                                 client_id="YOUR_APP_CLIENT_ID",
                                 client_secret="YOUR_APP_CLIENT_SECRET"))

random_pop_song_json: str = get_random(spotify=spotify_client, type="track", genre="pop")
```

## How it works

The randomization works by selecting a random letter to search for and randomly picking one of the result elements. The number of results can be changed with the `limit` parameter. The `offset_min` and `offset_max` parameters can optionally be used to influence the search result [offset](https://developer.spotify.com/documentation/web-api/reference/#/operations/search). 
