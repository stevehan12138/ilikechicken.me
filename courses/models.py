from django.db import models
from martor.models import MartorField

# Create your models here.
class Course(models.Model):
    course_name = models.CharField(max_length=100)
    description = models.TextField(max_length=100, default="")
    difficulty = models.IntegerField(choices=list(zip(range(1, 11), range(1, 11))), default=0)

    def __str__(self):
        return self.course_name

class Chapter(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    chapter_title = models.CharField(max_length=100)
    body = MartorField()
    
