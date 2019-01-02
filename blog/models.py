from django.db import models
from .errors import NoBlogFound  # here . means yei module
from ckeditor.fields import \
    RichTextField  # search for django ckeditor and open its github and look at installation procedure. pip install django-ckeditor, and add ckeditor to your installed apps settings, and then in models..
from sorl.thumbnail import ImageField


class Blog(models.Model):
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=50)
    content = RichTextField()  # don't forget () as we need to create object by calling constructor of that particular class, we are using ckeditor so don't use models.
    author = models.CharField(max_length=50)
    pub_date = models.DateTimeField(
        auto_now=True)  # this automatically provides date, at the time we create object, latest update of object time
    # image = models.ImageField() #pip install Pillow, in default value select 1 and give None. keep media root and media url in settings.py, and in urls.py
    image = ImageField() # this is due to sorl thumbnail. after this use makemigrations and then migrate
    def __str__(self):
        return self.title

    #
    @staticmethod  # for static method we don't need to create object of that class for calling
    def fetch_all():
        blogs = Blog.objects.all()  # get's blogs object in list. therefore we can calculate length

        if len(blogs) < 1:
            raise NoBlogFound  # note: we have to raise our exception class not return it

        return blogs


    # def fetch_all(self):
    #
    #
    #     blogs = Blog.objects.all() #get's blogs object in list. therefore we can calculate length
    #
    #     if len(blogs) < 1:
    #         raise NoBlogFound #note: we have to raise our exception class not return it
    #
    #     return blogs


class Comment(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50,
                              unique=False)  # if true can that particular email can comment only one time in our blog
    message = models.TextField()
    blog = models.ForeignKey(Blog,
                             on_delete=models.CASCADE)  # from blog.models import Blog #a.blog = Blog.objects.get(pk=2)

    def __str__(self):
        return self.email
