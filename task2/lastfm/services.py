import pylast
import requests
from django.conf import settings

BASE_URL = "http://audioscrobbler.com"

def call_lastfm_api(method, params=None):
    if params is None:
        params = {}
        
    default_params = {"method": method, "api_key": settings.LASTFM_API_KEY, "format": "json"}
    params.update(default_params)
    
    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        return {"error": str(e)}

def get_top_artists_by_country(country, limit=10):
    return call_lastfm_api("geo.getTopArtists", {"country": country, "limit": limit})

def get_top_tracks_by_country(country, limit=10):
    return call_lastfm_api("geo.getTopTracks", {"country": country, "limit": limit})

def search_artists(query, limit=10):
    return call_lastfm_api("artist.search", {"artist": query, "limit": limit})

def search_albums(query, limit=10):
    return call_lastfm_api("album.search", {"album": query, "limit": limit})

def search_tracks(query, limit=10):
    return call_lastfm_api("track.search", {"track": query, "limit": limit})
