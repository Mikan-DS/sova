from django.urls import path
from .views import *

urlpatterns = [
    path('', write_to_admin, name='ask moderator'),
    path('all', appeals, name='appeals'),
    path('<int:user_id>', answer_to_user, name='answer user'),
]