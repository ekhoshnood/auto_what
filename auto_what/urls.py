from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.conf import settings

from .views import home_screen
from account.views import registration_view, logout_view, login_view, accoutn_view, must_authenticate_view
from iframe_test.views import iframe
from django.contrib.auth import views as auth_views
from redditpage.views import reddit

urlpatterns = [
    path('', home_screen, name="home"),
    path('admin/', admin.site.urls),
    path('training', include('course_training.urls')),
    path('shakhsi', include('personal.urls')),
    path('register/', registration_view, name="register"),
    path('logout/', logout_view, name="logout"),
    path('login/', login_view, name="login"),
    path('account/', accoutn_view, name="account"),
    path('iframe/', iframe, name="iframe"),
    path('reddit/', reddit, name="reddit"),
    path('blog/', include('blog.urls', 'blog')),
    path('must_authenticate/', must_authenticate_view, name="must_authenticate"),

    # Password reset links (ref: https://github.com/django/django/blob/master/django/contrib/auth/views.py)
    # build in views to customize django built in pass reset
    path('password_change/done/',
         auth_views.PasswordChangeDoneView.as_view(template_name='registration/password_change_done.html'),
         name='password_change_done'),

    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='registration/password_change.html'),
         name='password_change'),

    path('password_reset/done/',
         auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_done.html'),
         name='password_reset_done'),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),

    path('reset/done/',
         auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'),
         name='password_reset_complete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
