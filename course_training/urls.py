from django.contrib import admin
from django.urls import path
from .views import course_training_page


urlpatterns = [
    path('', course_training_page, name="training"),
]
