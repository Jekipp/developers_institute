from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('students/', views.all_students, name='students'),
    path('students/add', views.add_student, name='add-student'),
    path('student/<int:student_id>', views.student, name='student'),

    path('subjects/', views.SubjectList.as_view(), name='subjects'),
    path('subject/<int:pk>/', views.SubjectDetails.as_view(), name='subject'),
    

    path('clearlocker/<int:student_id>', views.clearlocker, name='clearlocker'),
    path('home/', views.home, name='home'),
    path('reg/', views.reg, name='reg'),

    path('index/', views.index, name='blah'),
    path('index/<int:id>', views.index, name='blah'),
]