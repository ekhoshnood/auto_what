from django.urls import path
from blog.views import (
    create_blog_view,
)

# parameter to give the name
# whenever we creat a urls inside an app that's not inside the main url we need to create an app name parameter
# this is required step
app_name = 'blog'

urlpatterns = [
    path('create', create_blog_view, name="create"),
]
