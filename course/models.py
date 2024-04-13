from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# Create groups


class Course(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to='course_images/')
    instructor = models.ForeignKey(User, on_delete=models.CASCADE)
    duration = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.title = self.title.lower()
        super().save(*args, **kwargs)
    def __str__(self):
        return self.title
    



class Lessons(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    video = models.FileField(blank=True, null=True, upload_to='course_videos/')
    content = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
