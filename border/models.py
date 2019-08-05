from django.db import models

class Border(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=30)
    text = models.TextField(max_length=500)
    photo = models.ImageField(upload_to='border/static/', default = 'photos/no_image.png')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title