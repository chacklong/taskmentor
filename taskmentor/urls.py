# /taskmentor/urls.py

from django.contrib import admin
from django.urls import include, path
from taskmanager.views.general_views import home

urlpatterns = [
    path("admin/", admin.site.urls),
    path('taskmanager/',include('taskmanager.urls')),
    path('', home, name='home'),
]
