from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, Course, Comment
from django import forms

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('first_name' , 'last_name' , 'username',  'email', 'password1', 'password2', 'role')


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['title', 'content', 'image', 'instructor', 'duration']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'