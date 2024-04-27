from django.shortcuts import render
from course.models import Course, Lessons
from .serializer import CourseSerializer, LessonSerializer
from rest_framework import generics

# Create your views here.

class CourseAPIView(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer



# class LessonAPIView(generics.ListAPIView):
#     serializer_class = LessonSerializer

#     # def get_queryset(self):
#     #     course_id = self.kwargs.get('pk')
#     #     return  Lessons.objects.filter(pk=course_id)
# class LessonAPIView(generics.ListAPIView):
#     serializer_class = LessonSerializer

#     def get_queryset(self):
#         # Get the title from URL parameters and replace hyphens
#         title = self.kwargs.get.replace('-', '')
        
#         # Get the lesson id from URL parameters
#         lesson_id = self.kwargs.get('lesson_id')
        
#         # Retrieve the lesson object
#         lesson_dt = get_object_or_404(Lessons, id=lesson_id)
        
#         # Filter lessons based on the associated course title
#         return Lessons.objects.filter(course__title=title)
