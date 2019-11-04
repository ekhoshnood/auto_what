from django.contrib import admin
from django.urls import path
from .views import personal_page


urlpatterns = [
    path('', personal_page),
    path('admin/', admin.site.urls),
]
