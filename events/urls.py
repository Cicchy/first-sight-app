from django.urls import path
from . import views


urlpatterns = [
    path('events/', views.events, name='events_home'),
    path('events/<int:year>/', views.events, name='events'),
    path('event/<str:event_key>/', views.event, name='event'),
]