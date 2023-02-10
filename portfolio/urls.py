from django.urls import path
from .views import *

urlpatterns = [

    path('generator', generator, name='port_generator')

]