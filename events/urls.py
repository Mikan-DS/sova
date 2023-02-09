
from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="index"),
    path('events/', events, name="events"),
    path('events/create', events, name="create event"),
    path('events/<int:event_id>/', event, name="event"),
]