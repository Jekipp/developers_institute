from django.shortcuts import render, HttpResponse, redirect
from django.db import IntegrityError
from django.contrib import messages

from django.views import View, generic

from .models import Student, Subject
from .forms import StudentForm

import json
from faker import Faker


class SubjectList(generic.ListView):
    model = Subject
    template_name = 'subjects.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['extra_data'] = "This is some extra stuff"
        return context


class SubjectDetails(generic.DetailView):
    model = Subject
    template_name = 'subject.html'


# class AddSubject(View):

#     def get(self, request):
#         return render(request, 'add_subject.html', {'form': SubjectForm()})

#     def post(self, request):
#         form = SubjectForm(request.POST) 
#         if form.is_valid():
#             form.save()
#             #etc etc



def all_students(request):
    students = Student.objects.all()  # SELECT * FROM student_students  QUERYSET
    return render(request, 'students.html', {'students': students})


def student(request, student_id):
    student = Student.objects.get(id=student_id) # SELECT * FROM student_students  WHERE id = student_id LIMIT 1
    return render(request, 'student.html', {'student': student})
    

def add_student(request):

    if request.method == "GET":
        return render(request, 'add_student.html', {'form': StudentForm()})

    if request.method == "POST":
        form = StudentForm(request.POST) # A form bound to the POST data
        if form.is_valid():
            form.save()
            messages.success(request, 'Student Saved!', extra_tags="text-success")
            return redirect('students')
        else:
            messages.warning(request, 'Student Already Exists', extra_tags="text-danger")
            return render(request, 'add_student.html', {'form': form})


def clearlocker(request, student_id):
    student = Student.objects.get(id=student_id)
    student.locker.reset()
    return all_students(request)


def home(request):
    # Pretend this is fetching from the database...
    username = "Jon"
    # fav_fruits = ["apples", "peaches", "streetcats"]
    fav_fruits = [""]

    data_for_template = {
        'name': username, 
        'fruits': fav_fruits,
        }

    return render(request, 'home.html', data_for_template)


def index(request, id=None):
    return render(request, 'index.html', {'num': id})



def reg(request):

    if request.method == "GET":
        return render(request, 'reg.html')

    if request.method == "POST":
        f = Faker()

        fullname = request.POST.get('fullname')
        subject = request.POST.get('subject')

        fname, lname = fullname.split(" ")

        student = Student.objects.get_or_create(first_name=fname, last_name=lname)
        subject = Subject.objects.get(name=subject)
        student.subject_set.add(subject)

        return HttpResponse(f"Success. Student {fullname} was enrolled")
