from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login , logout
from .models import Course, Lessons, Comment, CustomUser
from .forms import CustomUserCreationForm, CourseForm, CommentForm
from django.contrib.auth.decorators import login_required
# Create your views here.

def register_views(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request,'auth/register.html', {'form' : form})
        

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
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


@login_required
def logout_view(request):
    logout(request)
    return redirect('home')


def user_page(request, pk):
    if request.user.is_authenticated:
        user = get_object_or_404(CustomUser, pk=pk)
        context = { 
            'user' : user
        }
        return render(request, 'pages/user_page.html', context)
    else:
        return render(request, 'pages/404.html')
        
def delete_user(request):
    delete = CustomUser.objects.get
    delete.save()
    return redirect('register')


def home(request):
    courses  = Course.objects.all()

    context = {
        'courses' : courses,

    }
    return render(request, 'pages/home.html', context)


@login_required
def add_course(request):
    if request.user.role == 'instructor':
        if request.method == 'POST':
            form = CourseForm(request.POST, request.FILES)
            if form.is_valid():
                course = form.save(commit=False)
                course.instructor = request.user
                course.save()
                return redirect('home')
        else:
            form = CourseForm()
        return render(request, 'pages/add_course.html', {'form': form})
    else:
        # return render(request, 'pages/404.html', status=404)
        return redirect('home')


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
        # Replace spaces with hyphens in the title
        title = title.replace('-', '')
        # Retrieve the lesson object
        lesson_dt = get_object_or_404(Lessons, id=lesson_id)
    
        if request.method == 'POST':
            # Retrieve name and comment from POST data
            form = CommentForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('lessons_details', lesson_id=lesson_id, title=title)

        # Pass the lesson object to the template
        return render(request, 'pages/lesson.html', {'lesson_dt': lesson_dt})
    else:
        return redirect('login')
