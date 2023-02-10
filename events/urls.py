
from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="index"),
    path('events/', events, name="events"),
    path('plans/', plans, name="plans"),
    path('events/create', create_event, name="create event"),
    path('events/<int:event_id>/', event, name="event"),
    path('events/<int:event_id>/add_plan', add_plan, name="add plan"),
    path('events/<int:event_id>/<int:plan_id>', plan, name="plan"),

    path('events/edit/<int:event_id>', edit_event, name="edit event"),
    path('events/edit/<int:event_id>/delete', delete_event, name="delete event"),

]