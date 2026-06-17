from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class BlogModel(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    content = models.TextField()
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

class Comment(models.Model):
    blog = models.ForeignKey(
        BlogModel,
        on_delete=models.CASCADE,
        related_name='comments'
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    content = models.TextField()

    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.blog.title}"