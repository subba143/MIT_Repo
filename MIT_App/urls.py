from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import InstituteViewSet, CourseViewSet, StudentViewSet
from .views import search, profile_detail

router = DefaultRouter()
router.register(r'institutes', InstituteViewSet)
router.register(r'courses', CourseViewSet)
router.register(r'students', StudentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('search/', search, name='search'),
    path('profile/<int:profile_id>/', profile_detail, name='profile_detail'),
]




