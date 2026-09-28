from django.shortcuts import render
from django.http import JsonResponse
from . import services

def geo_data_view(request):
    country = request.GET.get("country", "India")
    data_type = request.GET.get("type", "artists")  # 'artists' or 'tracks'
    
    if data_type == "tracks":
        data = services.get_top_tracks_by_country(country)
    else:
        data = services.get_top_artists_by_country(country)
        
    return JsonResponse(data)

def search_view(request):
    query = request.GET.get("q", "")
    search_type = request.GET.get("type", "artist")  # 'artist', 'album', or 'track'
    
    if not query:
        return JsonResponse({"error": "Query parameter 'q' is required"}, status=400)
        
    if search_type == "album":
        data = services.search_albums(query)
    elif search_type == "track":
        data = services.search_tracks(query)
    else:
        data = services.search_artists(query)
        
    return JsonResponse(data)
