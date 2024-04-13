from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login , logout
from .models import Course, Lessons
from django.contrib.auth.decorators import login_required

# Create your views here.

def register_views(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request,'auth/register.html', {'form' : form})
        

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():  # Corrected: Added parentheses after is_valid
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                form.add_error(None, 'Invalid username or password')
    else:
            form = AuthenticationForm()
    return render(request, 'auth/login.html', {'form' : form})



def logout_view(request):
    logout(request)
    return redirect('home')



def home(request):
    courses  = Course.objects.all()

    context = {
        'courses' : courses,

    }
    return render(request, 'pages/home.html', context)



def search_view(request):
    query = request.GET.get('query')
    results = []
    if query:
        results = Course.objects.filter(title__icontains=query)
    print(results)
    context = {
        'query': query,
        'results': results
    }
    return render(request, 'pages/search_course.html', context)


def course_details(request, title):
    title = title.replace('-', ' ')
    course = get_object_or_404(Course, title=title)   
    lessons = course.lessons_set.all()
    return render(request, 'pages/course_dt.html', {'course': course, 'lessons': lessons})



def lessons_details(request, lesson_id, title):
    if request.user.is_authenticated:
        title = title.replace('-', '')
        lesson_dt = get_object_or_404(Lessons, id=lesson_id)
        return render(request, 'pages/lesson.html', {'lesson_dt': lesson_dt})
    else:
        return redirect('login')