from django.contrib import admin
from django.urls import path, include
from .views import home_screen
from account.views import registration_view, logout_view, login_view, accoutn_view


urlpatterns = [
    path('', home_screen, name="home"),
    path('admin/', admin.site.urls),
    path('training', include('course_training.urls')),
    path('shakhsi', include('personal.urls')),
    path('register/', registration_view, name="register"),
    path('logout/', logout_view, name="logout"),
    path('login/', login_view, name="login"),
    path('account/', accoutn_view, name="account"),
]
