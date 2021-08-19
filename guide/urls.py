from django.urls import path
from .views import TravelListView
urlpatterns = [
    path('guide/', TravelListView.as_view(), name='travel_list_url' )
]