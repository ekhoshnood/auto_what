from django.contrib import admin
from django.urls import path, include
from . import views as Vmain


urlpatterns = [
    path('', Vmain.home_screen),
    path('admin/', admin.site.urls),
]
