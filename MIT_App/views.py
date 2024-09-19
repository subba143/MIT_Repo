from django.shortcuts import render
from rest_framework import viewsets
from .models import Institute, Course, Student, Profile
from .serializers import InstituteSerializer, CourseSerializer, StudentSerializer, ProfileSerializer

# Create your views here.

class InstituteViewSet(viewsets.ModelViewSet):
    queryset = Institute.objects.all()
    serializer_class = InstituteSerializer

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Institute, Course, Student, Profile

@api_view(['POST'])
def search(request):
    search_term = request.data.get('search', '')
    institute_results = Institute.objects.filter(institute_name__icontains=search_term)
    course_results = Course.objects.filter(course_name__icontains=search_term)
    student_results = Student.objects.filter(student_name__icontains=search_term)
    profile_results = Profile.objects.filter(name__icontains=search_term)

    results = []

    for profile in profile_results:
        results.append({
            "institute_name": profile.student.institute.institute_name,
            "course_name": profile.student.course.course_name,
            "student_name": profile.student.student_name,
            "joining_date": profile.student.joining_date.strftime('%d %b %Y'),
            "profile_name": profile.name
        })

    return Response(results)

@api_view(['POST'])
def search(request):
    search_term = request.data.get('search', '')

    profiles = Profile.objects.filter(name__icontains=search_term)

    results = []
    for profile in profiles:
        results.append({
            "name": profile.name,
            "photo": profile.photo.url,
            "resume": profile.resume.url
        })

    return Response(results)



from django.shortcuts import render, redirect
from .forms import ProfileForm

def upload_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('profile_success')
    else:
        form = ProfileForm()
    return render(request, 'upload_profile.html', {'form': form})

from django.shortcuts import render, get_object_or_404
def profile_detail(request, profile_id):
    profile = get_object_or_404(Profile, id=profile_id)
    return render(request, 'profile_detail.html', {'profile': profile})
