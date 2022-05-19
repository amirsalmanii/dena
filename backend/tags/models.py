from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, allow_unicode=True, blank=True)

    class Meta:
        ordering = ("-id",)

    def save(self, *args, **kwargs):
        self.slug = self.name.replace(" ", "-")
        super(Tag, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
