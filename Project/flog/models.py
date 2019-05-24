# built-in import
from django.db import models

# manual import
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# django treat data as OOP with ORM


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    # on_delete=models.CASCADE => if author is deleted, so are his posts
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title}"

    # reverse route after new post is added
    def get_absolute_url(self):
        return reverse("post-detail", kwargs={"pk": self.pk})
