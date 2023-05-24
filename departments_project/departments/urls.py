from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('profile/<str:name>/<int:pk>/', views.profile, name='profile-data'),
    path('register/', views.test_form, name='register'),
]
