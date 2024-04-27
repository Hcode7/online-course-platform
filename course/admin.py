from django.contrib import admin
from .models import Course, Lessons, ExamQuestion, ExamAnswer, Comment

# Register your models here.


admin.site.register(Course)
admin.site.register(Lessons)
admin.site.register(ExamQuestion)
admin.site.register(ExamAnswer)
admin.site.register(Comment)