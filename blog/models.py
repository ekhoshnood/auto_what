from django.db import models
from django.db.models.signals import pre_save, post_delete
from django.utils.text import slugify
from django.conf import settings
from django.dispatch import receiver


# method to define the file upload location
def upload_location(instance, filename):
    file_path = 'blog/{author_id}/{title}-{filename}'.format(
        author_id=str(instance.author.id),  # taking the id whos uploading it
        title=str(instance.title),  # title of the blog post
        filename=filename  # the name of the file that coming from the computer
    )
    return file_path


class BlogPost(models.Model):
    title = models.CharField(max_length=50, null=False, blank=False)
    body = models.TextField(max_length=5000, null=False, blank=False)
    image = models.ImageField(upload_to=upload_location, null=False, blank=False)
    date_published = models.DateTimeField(auto_now_add=True, verbose_name="date published")
    date_updated = models.DateTimeField(auto_now_add=True, verbose_name="date updated")
    # settings.AUTH_USER_MODEL #
    # in setting we have auth_user_model that is set to account.model so instead of importing account model
    # we are saying look for whatever account or user authenticate kind of model we have associated with this project
    # for users and use that
    # ForeignKey #
    # it looks to our account table and use foreignkey relationship to that table, so
    # the user that creates it will be associated with their account
    # on_delete=models.CASCADE #
    # defines what happens if this blog post is deleted so
    # models.CASCADE MEANS # delete anything that you see that is associated with this blog post ( images, ...)
    # so don't delete the account but every thing else associated with it
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # slug
    # is a web development thing
    # it is essentialy url after main site address
    slug = models.SlugField(blank=True, unique=True)

    # to return the default object
    def __str__(self):
        return self.title


# if this blog post is deleted, i want to also delete the image that is associated
# if we dont build this so image would stay on database and on our contect delevery network
@receiver(post_delete, sender=BlogPost)
def submission_delete(sender, instance, **kwargs):
    instance.image.delete(False)


# this will be called before the blog post is committed to database
def pre_save_blog_post_receiver(sender, instance, *args, **kwargs):
    # if there is no slug created yet => create this slug with this format, so it will be unique
    if not instance.slug:
        instance.slug = slugify(instance.author.username + "-" + instance.title)


# wire up our pre_save receiver
# whenever a blog post attends to save to database => call this function (pre_save_blog_post_receiver)
pre_save.connect(pre_save_blog_post_receiver, sender=BlogPost)
