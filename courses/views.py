from django.shortcuts import get_object_or_404, render
from django.views import generic
from .models import *

# Create your views here.
class CourseList(generic.ListView):
    template_name = 'courses/index.html'
    context_object_name = 'courses'

    def get_queryset(self):
        return Course.objects.all()

class CourseView(generic.DetailView):
    context_object_name = 'course'
    template_name = 'courses/course.html'
    def get_object(self):
        return get_object_or_404(Course, course_name=self.kwargs['course'])