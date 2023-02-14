from django.urls import path

from events.views import inprogress
from .views import *

urlpatterns = [

    path('', FAQ, name='FAQ'),
    path('recyclables', recyclables, name='recyclables'),


]