from django.urls import path
from . import views

urlpatterns = [
    path('api/geo/', views.geo_data_view, name='geo_data'),
    path('api/search/', views.search_view, name='search'),
]