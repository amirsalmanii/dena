from django.db import models

class Category(models.Model):
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=254, unique=True, allow_unicode=True, blank=True)

    class Meta:
        ordering = ('-id',)
    
    def save(self, *args, **kwargs):
        self.slug = self.name.replace(' ', '-')
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
    

