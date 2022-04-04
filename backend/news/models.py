from django.db import models
from accounts.models import User

class NewsCategory(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=254, unique=True, allow_unicode=True, blank=True)

    class Meta:
        ordering = ("-id",)

    def save(self, *args, **kwargs):
        self.slug = self.name.replace(" ", "-")
        super(NewsCategory, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class News(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    news_category = models.ForeignKey(NewsCategory, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    title_image = models.ImageField(upload_to='news', blank=True)
    body = models.TextField(blank=True)
    created_at = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ("-id",)
        
    def __str__(self):
        return self.title
