from django.contrib import admin
from .models import Institute, Course, Student, Profile
# Register your models here.
admin.site.register(Institute)
admin.site.register(Course)
admin.site.register(Student)
admin.site.register(Profile)