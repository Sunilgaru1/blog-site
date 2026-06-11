from django.db import models
from django.utils import timezone

# Create your models here.

class BlogModel(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
