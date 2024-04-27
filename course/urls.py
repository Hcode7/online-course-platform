from django.urls import path
from . import views

urlpatterns  = [
    path('register/', views.register_views, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    
    path('user/<int:pk>/', views.user_page, name='user'),
    # path('delete/user/')

    path('', views.home, name='home'),
    path('create_course/', views.add_course, name='create_course'),
    path('search/', views.search_view, name='search'),
    path('course/<str:title>/', views.course_details, name='course_details'),
    path('course/<str:title>/lessons/<int:lesson_id>', views.lessons_details, name='lessons'),

]

LOGIN_URL = 'login/'