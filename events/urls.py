
from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="index"),
    path('events/', events, name="events"),
    path('plans/', plans, name="plans"),

    path('events/create', create_event, name="create event"),
    path('events/<int:event_id>/', event, name="event"),
    path('events/edit/<int:event_id>', edit_event, name="edit event"),
    path('events/edit/<int:event_id>/delete', delete_event, name="delete event"),


    path('events/<int:event_id>/add_plan', add_plan, name="add plan"),

    path('events/<int:event_id>/<int:plan_id>', plan, name="plan"),
    path('events/<int:event_id>/edit/<int:plan_id>', edit_plan, name="edit plan"),
    path('events/<int:event_id>/dit/<int:plan_id>/delete', delete_plan, name="delete plan"),

    path('events/<int:event_id>/<int:plan_id>', plan, name="plan"),
    path('events/<int:event_id>/edit/<int:plan_id>', edit_plan, name="edit plan"),
    path('events/<int:event_id>/edit/<int:plan_id>/delete', delete_plan, name="delete plan"),
    path('events/<int:event_id>/edit/<int:plan_id>/create_shedule', add_shedule, name="create shedule"),
    path('events/<int:event_id>/edit/<int:plan_id>/edit_shedule', edit_shedule, name="edit shedule"),

    path('events/<int:event_id>/edit/<int:plan_id>/report/create', create_report, name="create report"),
    path('events/<int:event_id>/edit/<int:plan_id>/report/<int:report_id>', create_report, name="edit report"),

    path('reports/<int:report_id>', read_report, name='report'),
    path('reports/edit/<int:report_id>', edit_report, name='edit report'),
    path('reports/edit/delete_image/<int:image_id>', delete_image, name='delete image'),
    path('reports/edit/<int:report_id>/add_images/', add_images, name='add images'),
]