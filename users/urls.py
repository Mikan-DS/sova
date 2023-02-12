from django.urls import path
from .views import *

urlpatterns = [
    path('', profile, name="profile"),
    path('edit', edit_profile, name="edit profile"),
    path('login', login_user, name="login"),
    path('logout', logout_user, name="logout"),

]