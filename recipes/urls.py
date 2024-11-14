from django.urls import path
from recipes.views import home, contato, sobre



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('sobre/', sobre),
    path('contato/', contato),
]