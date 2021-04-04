from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "categories"
        verbose_name_plural = "Category"

    def __str__(self):
        return self.name


class News(models.Model):
    class NewsStatus(models.IntegerChoices):
        draft = 1
        published = 2

    title = models.CharField(max_length=225)
    cover = models.ImageField(upload_to='images')
    content = models.TextField()
    excerpt = models.TextField()
    status = models.IntegerField(choices=NewsStatus.choices)

    published_at = models.DateTimeField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category)

    class Meta:
        db_table = "news"
        verbose_name_plural = "News"

    def __str_(self):
        return self.name


class Comment(models.Model):

    name = models.CharField(max_length=100)
    emial = models.EmailField()
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    news = models.ForeignKey(News, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
