"""sova URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf.urls.static import static
from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path, include

from sova import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('events.urls')),
    path('user/', include('users.urls')),
    path('appeals/', include('appeals.urls')),
    path('portfolio/', include('portfolio.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


def back_to_home(request, *args, **kwargs):
    return redirect('index')


handler404 = handler400 = handler403 = handler500 = back_to_home
