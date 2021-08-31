from django.db import models

# Create your models here.

class News(models.Model):
    title = models.CharField(max_length=150)  # max_length=150обязат. атрибут
    content = models.TextField(blank=True)  # blank=True необязательно к заполнению
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title




