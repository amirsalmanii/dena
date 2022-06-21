import os
from io import BytesIO
from PIL import Image
from django.core.files.base import ContentFile
from django.db import models
from accounts.models import User
from ckeditor_uploader.fields import RichTextUploadingField
THUMB_SIZE = (400, 400)


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
    thumbnail = models.ImageField(upload_to="news/th/", blank=True, null=True)
    body = RichTextUploadingField()
    summery = models.TextField(blank=True, null=True, default="")
    hashtag = models.TextField(blank=True, null=True, default="")
    created_at = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ("-id",)
        
    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.make_thumbnail():
            pass
        super(News, self).save(*args, **kwargs)

    def make_thumbnail(self):
        # if user set image
        if self.title_image:
            image = Image.open(self.title_image)
            image.thumbnail(THUMB_SIZE, Image.ANTIALIAS)

            thumb_name, thumb_extension = os.path.splitext(self.title_image.name)
            thumb_extension = thumb_extension.lower()

            thumb_filename = thumb_name + "_thumb" + thumb_extension

            if thumb_extension in [".jpg", ".jpeg"]:
                FTYPE = "JPEG"
            elif thumb_extension == ".gif":
                FTYPE = "GIF"
            elif thumb_extension == ".png":
                FTYPE = "PNG"
            else:
                return False  # Unrecognized file type

            # Save thumbnail to in-memory file as StringIO
            temp_thumb = BytesIO()
            image.save(temp_thumb, FTYPE)
            temp_thumb.seek(0)

            # set save=False, otherwise it will run in an infinite loop
            self.thumbnail.save(
                thumb_filename, ContentFile(temp_thumb.read()), save=False
            )
            temp_thumb.close()

            return True
        else:
            return ""
