from django.contrib import admin
from django.urls import path, include
from .views import home_screen


urlpatterns = [
    path('', home_screen, name="home"),
    path('admin/', admin.site.urls),
    path('training', include('course_training.urls')),
    path('shakhsi', include('personal.urls'))
]
