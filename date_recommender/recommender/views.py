from django.shortcuts import render
from django.conf import settings
from .models import DatePlace
from django.http import JsonResponse

def main_view(request):
    places = DatePlace.objects.all()
    return render(request, 'recommender/main.html', {
        'places': places,
        'google_maps_api_key': settings.GOOGLE_MAPS_API_KEY
    })

def get_places(request):
    region = request.GET.get('region', '')
    if region:
        places = DatePlace.objects.filter(region=region)
    else:
        places = DatePlace.objects.all()
    
    places_data = [{
        'id': place.id,
        'name': place.name,
        'category': place.category,
        'latitude': place.latitude,
        'longitude': place.longitude,
        'address': place.address,
        'description': place.description,
    } for place in places]
    
    return JsonResponse({'places': places_data})
