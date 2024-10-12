from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_view, name='main'),
    path('get_places/', views.get_places, name='get_places'),
    path('add/', views.add_date_place, name='add_date_place'),
]
