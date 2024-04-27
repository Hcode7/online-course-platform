from django.urls import path
from . import views

urlpatterns = [
    path('courses/', views.CourseAPIView.as_view()),
    # path('api/course/<str:title>/lesson/<int:pk>/', views.LessonAPIView.as_view(), name='lesson-detail'),
]