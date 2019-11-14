from django import forms
from .models import BlogPost


class CreateBlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'body', 'image']


class UpdateBlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'body', 'image']

    # we are custom  save method for the form and the reason for that is that because
    # we want to specify only these fields as change and dont want to change other(author)
    def save(self, commit=True):  # this will only be called if commit=true
        blog_post = self.instance # grt reference to blog post
        # for inside a form and that form has been declared valid so if inside view  we write form is valid
            # that means we have access to clean data so in other form the form data so
        blog_post.title = self.cleaned_data['title']
        blog_post.body = self.cleaned_data['body']

        if self.cleaned_data['image']: # if form has image set it otherwise dont change the image
            blog_post.image = self.cleaned_data['image']

        if commit: # if commit is true
            blog_post.save()
        return blog_post
