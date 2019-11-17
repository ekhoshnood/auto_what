from operator import attrgetter
from django.shortcuts import render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from blog.models import BlogPost
from blog.views import get_blog_queryset

BLOG_POSTS_PER_PAGE = 2
def reddit(request):
    context={}
    query = ""
    if request.GET:     # if there is a get request then
        query = request.GET.get('q', '') # search for parameter q
        context['query'] = str(query) # wether there is or is not a parameter q we will pass it to context

    # sorted will sort the list based on the key date updated and we will reverse it to show newest post on top
    # blog_posts = sorted(BlogPost.objects.all(), key=attrgetter('date_updated'), reverse=True)
    blog_posts = sorted(get_blog_queryset(query), key=attrgetter('date_updated'), reverse=True)

    # pagination
    page = request.GET.get('page', 1)
    blog_post_paginator = Paginator(blog_posts, BLOG_POSTS_PER_PAGE)

    try:
        blog_posts = blog_post_paginator.page(page)
    except PageNotAnInteger:
        blog_posts = blog_post_paginator.page(BLOG_POSTS_PER_PAGE)
    except EmptyPage:
        blog_posts = blog_post_paginator.page(blog_post_paginator.num_pages)

    context['blog_posts'] = blog_posts


    return render(request, "reddit/home.html", context)