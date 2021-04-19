from django.db import models
from ckeditor.fields import RichTextField
from django.utils import timezone

# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    body = RichTextField()
    last_edited = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return self.title