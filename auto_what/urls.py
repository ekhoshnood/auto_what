from django.contrib import admin
from django.urls import path, include
from .views import home_screen


urlpatterns = [
    path('', home_screen),
    path('admin/', admin.site.urls),
    path('shakhsi', include('personal.urls'))
]
