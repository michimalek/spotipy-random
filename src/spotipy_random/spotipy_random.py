from spotipy import Spotify
from typing import Any, Optional
import random


def get_wildcard() -> str:
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    wildcard = random.choice(alphabet)

    rand = random.randint(0,2)
    if rand == 0:
        wildcard = f"%{wildcard}"
    if rand == 1:
        wildcard = f"{wildcard}%"
    if rand == 2:
        wildcard = f"%{wildcard}%"

    return wildcard


def get_random(spotify: Spotify,
               limit: int = 10,
               offset_min: int = 0,
               offset_max: int = 20,
               type: str = "track",
               market: Any = None,
               album: str = None,
               artist: str = None,
               track: str = None,
               year: str = None,
               upc: str = None,
               tag_hipster: bool = None,
               tag_new: bool = None,
               isrc: str = None,
               genre: str = None,
               ) -> dict:

    if offset_max > 1000:
        raise ValueError("The maximum allowed offset is 1000.")

    types: list = type.split(',')
    random_type: str = random.choice(types)
    types = [random_type]

    offset: int = random.randint(offset_min, offset_max)

    wildcard: str = get_wildcard()
    q: str = f"{wildcard}"

    if len(types) == 0:
        raise ValueError("Type must contain at least one valid search type.")

    artist_filter_supported: bool = not (("playlist" or "show" or "episode") in types)
    album_filter_supported: bool = not (("artist" or "playlist" or "show" or "episode") in types)
    genre_filter_supported: bool = not (("album" or "playlist" or "show" or "episode") in types)
    track_filter_supported: bool = not (("artist" or "album" or "playlist" or "show" or "episode") in types)
    year_filter_supported: bool = not (("artist" or "playlist" or "show" or "episode") in types)
    isrc_filter_supported: bool = not (("artist" or "album" or "playlist" or "show" or "episode") in types)
    upc_filter_supported: bool = not (("artist" or "track" or "playlist" or "show" or "episode") in types)
    tag_hipster_filter_supported: bool = not (("artist" or "track" or "playlist" or "show" or "episode") in types)
    tag_new_filter_supported: bool = not (("artist" or "track" or "playlist" or "show" or "episode") in types)

    if artist_filter_supported and artist is not None:
        q += f" artist:{artist}"

    if album_filter_supported and album is not None:
        q += f" album:{album}"

    if track_filter_supported and track is not None:
        q += f" track:{track}"

    if year_filter_supported and year is not None:
        q += f" year:{year}"

    if genre_filter_supported and genre is not None:
        q += f" genre:{genre}"

    if isrc_filter_supported and isrc is not None:
        q += f" isrc:{isrc}"

    if upc_filter_supported and upc is not None:
        q += f" upc:{upc}"

    if tag_hipster_filter_supported and tag_hipster is not None:
        q += f" {'tag:hipster' if tag_hipster else ''}"

    if tag_new_filter_supported and tag_new is not None:
        q += f" {'tag:new' if tag_new else ''}"

    result = spotify.search(q, limit, offset, type, market)
    random_type_result_key: str = f"{random_type}s"

    if result is None:
        raise ValueError("No result was returned.")

    try:
        element: dict = result[random_type_result_key]["items"][0]
    except KeyError:
        raise KeyError("The result could not be parsed.")

    return element
