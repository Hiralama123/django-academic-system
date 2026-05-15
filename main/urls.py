from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('dashboard/', views.dashboard, name='dashboard'),
    # Student Urls
    path('students/', views.student_list, name='student_list'),
    path('students/add/', views.student_create, name='student_add'),
    path('students/edit/<int:id>/', views.student_update, name='student_edit'),
    path('students/delete/<int:id>/', views.student_delete, name='student_delete'),
    # Course URLs
    path('courses/', views.course_list, name='course_list'),
    path('courses/add/', views.course_create, name='course_add'),
    path('courses/edit/<int:id>/', views.course_update, name='course_edit'),
    path('courses/delete/<int:id>/', views.course_delete, name='course_delete'),
    # Registration Urls
    path('registrations/', views.registration_list, name='registration_list'),
    path('registrations/add/', views.registration_create, name='registration_add'),
    path('registrations/edit/<int:id>/', views.registration_update, name='registration_edit'),
    path('registrations/delete/<int:id>/', views.registration_delete, name='registration_delete'),


]