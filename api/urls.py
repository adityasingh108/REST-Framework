from django.urls import path,include
from .import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('student',views.StudentViewset,basename='studentapi')


urlpatterns = [
    path('',include(router.urls)),
    path('auth/',include('rest_framework.urls')),   ## Showing Login Logout button in navbar
]
