from django.contrib import admin
from django.urls import path, include, path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('recipes.urls')),
]