from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth.decorators import login_required
from .models import DatePlace, DateCourse, DateCoursePlace
from django.http import JsonResponse
from .forms import DatePlaceForm
from django.contrib import messages
from django.views.decorators.http import require_POST
import json

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
        'category': place.get_category_display(),
        'latitude': place.latitude,
        'longitude': place.longitude,
        'address': place.address,
        'description': place.description,
    } for place in places]
    
    return JsonResponse({'places': places_data})

@login_required
def add_date_place(request):
    if request.method == 'POST':
        form = DatePlaceForm(request.POST)
        if form.is_valid():
            date_place = form.save(commit=False)
            date_place.save()
            messages.success(request, '새로운 데이트 장소가 추가되었습니다!')
            return redirect('main')
    else:
        form = DatePlaceForm()
    return render(request, 'recommender/add_date_place.html', {'form': form})

@login_required
def create_date_course(request):
    return render(request, 'recommender/create_date_course.html', {
        'google_maps_api_key': settings.GOOGLE_MAPS_API_KEY
    })

@login_required
@require_POST
def save_date_course(request):
    data = json.loads(request.body)
    course = DateCourse.objects.create(user=request.user, name=data['name'])
    for i, place in enumerate(data['places']):
        DateCoursePlace.objects.create(
            date_course=course,
            name=place['name'],
            latitude=place['lat'],
            longitude=place['lng'],
            visit_time=place['time'],
            order=i
        )
    return JsonResponse({'status': 'success'})
