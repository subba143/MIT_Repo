from django.db import models
# Create your models here.
class Institute(models.Model):
    institute_id = models.AutoField(primary_key=True)
    institute_name = models.CharField(max_length=100, unique=True)

class Course(models.Model):
    course_id = models.AutoField(primary_key=True)
    institute = models.ForeignKey(Institute, on_delete=models.CASCADE)
    course_name = models.CharField(max_length=100)

class Student(models.Model):
    student_id = models.AutoField(primary_key=True)
    institute = models.ForeignKey(Institute, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    student_name = models.CharField(max_length=100)
    joining_date = models.DateField()


class Profile(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='profile_pics/')
    resume = models.FileField(upload_to='resumes/')

    def __str__(self):
        return self.name
