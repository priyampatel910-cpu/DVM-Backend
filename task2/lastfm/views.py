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

import json
from django.shortcuts import render
from . import services

def home_view(request):
    context = {"current_country": "India", "current_type": "artists", "current_query": "", "current_search_type": "artist", "raw_json": None}

    if "country" in request.GET:
        country = request.GET.get("country", "India")
        data_type = request.GET.get("type", "artists")
        
        context["current_country"] = country
        context["current_type"] = data_type
        
        if data_type == "tracks":
            data = services.get_top_tracks_by_country(country)
        else:
            data = services.get_top_artists_by_country(country)

        context["raw_json"] = json.dumps(data, indent=2)

    elif "q" in request.GET:
        query = request.GET.get("q", "")
        search_type = request.GET.get("search_type", "artist")
        
        context["current_query"] = query
        context["current_search_type"] = search_type
        
        if query:
            if search_type == "album":
                data = services.search_albums(query)
            elif search_type == "track":
                data = services.search_tracks(query)
            else:
                data = services.search_artists(query)
                
            context["raw_json"] = json.dumps(data, indent=2)

    return render(request, "index.html", context)

