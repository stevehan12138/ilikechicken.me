from django.contrib import admin

# Register your models here.
from .models import *

class ChaptersInline(admin.StackedInline):
    model = Chapter
    extra = 1


class CourseAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,  {'fields': ['course_name', 'description', 'difficulty']})
    ]
    inlines = [ChaptersInline]

admin.site.register(Course, CourseAdmin)