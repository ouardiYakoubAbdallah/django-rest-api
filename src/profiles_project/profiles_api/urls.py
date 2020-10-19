from django.urls import path
from django.urls import include

from rest_framework.routers import DefaultRouter

from . import views 

router = DefaultRouter()
router.register('Profile', views.UserProfileViewSet)
router.register('Login', views.LoginViewSet, basename='Login')

urlpatterns = [
    #path('first/', views.FirstView.as_view(), name='First APIView'),
    path('', include(router.urls))
]