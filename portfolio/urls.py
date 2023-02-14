from django.urls import path

from events.views import inprogress
from .views import *

urlpatterns = [

    path('', portfolio, name='portfolio'),
    path('achievement-wall', achievement_wall, name='achievement wall'),
    path('raiting', raiting, name='raiting'),
    path('generator', inprogress, name='port_generator'),
    path('plan_<int:plan_id>/edit', edit_peoples_on_shedule, name='change shedule students'),
    path('plan_<int:plan_id>/edit/byhand', edit_peoples_byhand, name='change shedule students byhand'),
    path('plan/delete/<int:activity_id>', delete_student_from_plan, name='remove student from plan'),
    path('plan_<int:plan_id>/edit/raw', inprogress, name='change shedule students raw'),
    path('plan_<int:plan_id>/edit/excel', inprogress, name='change shedule students excel'),

]