from django.urls import path
from .views import fetch_map_data, fetch_all_data, get_detail, fetch_search_data, fetch_total_search
app_name = 'map'

urlpatterns = [
    path('', fetch_map_data),
    path('all', fetch_all_data),
    path('detail/<str:iri>', get_detail),
    path('search/<str:search>/<int:page>', fetch_search_data),
    path('search/<str:search>/total', fetch_total_search),
]