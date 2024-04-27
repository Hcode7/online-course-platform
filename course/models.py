from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('learner', 'Learner'),
        ('instructor', 'Instructor'),
    )
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    image = models.ImageField(upload_to='users_images/', blank=True, null=True)

    def __str__(self):
        return self.username

class Course(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to='course_images/')
    instructor = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
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
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class ExamQuestion(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    question = models.CharField(max_length=200)

    def __str__(self):
        return self.question

class ExamAnswer(models.Model):
    question = models.OneToOneField(ExamQuestion, on_delete=models.CASCADE)
    QUESTION_ANSWER_CHOICES = [
        ('1', 'Datatype and Primary Key constraint'),
        ('2', 'Name and datatype'),
    ]
    answer = models.CharField(max_length=1, choices=QUESTION_ANSWER_CHOICES)

    def __str__(self):
        return self.get_answer_display()


class Comment(models.Model):
    lesson = models.ForeignKey(Lessons, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.lesson.title, self.comment)