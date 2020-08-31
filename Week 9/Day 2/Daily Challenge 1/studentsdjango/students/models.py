from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=30, default='', unique=True)

    def __repr__(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return f"I'm a student called {self.first_name}"


class Locker(models.Model):
    number = models.IntegerField()
    pin = models.CharField(max_length=5, null=True)
    student = models.OneToOneField(Student, on_delete=models.SET_NULL, null=True)

    def reset(self):
        self.pin = None
        self.save()
        return self
        

class Car(models.Model):
    make = models.CharField(max_length=30)
    color = models.CharField(max_length=30)
    owner = models.ForeignKey(Student, on_delete=models.CASCADE) 


class Subject(models.Model):
    name = models.CharField(max_length=100)
    teacher_name = models.CharField(max_length=50)
    students = models.ManyToManyField(Student)

    def __repr__(self):
        return f"{self.name}"

    def __str__(self):
        return f"{self.name}"