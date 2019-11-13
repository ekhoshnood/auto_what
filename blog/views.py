from django.shortcuts import render, redirect
from .models import BlogPost
from .forms import CreateBlogPostForm
from account.models import Account


def create_blog_view(request):
    context = {}

    user = request.user

    if not user.is_authenticated:
        return redirect('must_authenticate')

    # either its going to be a post request or nothing at all
    # request.files = because we neet to upload an image as it is a blog posting
    form = CreateBlogPostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        # as there is some field required ( according to blog models, like author) so
        # we need to define some objects first before saving
        obj = form.save(commit=False) # this will create the form after all the fields are validated and
        # the reason we need to do that is because we need to set the author object to blog post because
        # that's not gonna set by default so thats why we need to do this[form.save(commit=False)]

        author = Account.objects.filter(email=user.email).first() # by default this[Account.objects.filter(email=user.email)]
        # will return the query set so we need to call this[first()] to actually to get the first item in that list
        # there should be one item though we have to call that[first()]
        obj.author = author # we need to set the author of object to author that we got
        obj.save() # then we will save that blog post to database
        form = CreateBlogPostForm() # after saving we want to reset everything so we will set the form to brand
        # new blog post form

    # last step to passing the form to view
    context['form'] = form

    return render(request, 'blog/create_blog.html', context)