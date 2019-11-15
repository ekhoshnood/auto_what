from django.shortcuts import render
from blog.models import BlogPost
from operator import attrgetter


def reddit(request):
    context={}
    query = ""
    if request.GET:
        query = request.GET['q']
        context['query'] = str(query)

    # sorted will sort the list based on the key date updated and we will reverse it to show newest post on top
    blog_posts = sorted(BlogPost.objects.all(), key=attrgetter('date_updated'), reverse=True)
    context['blog_posts'] = blog_posts

    return render(request, "reddit/home.html", context)