from django.urls import path,include

from . import views

app_name = 'master'
urlpatterns = [
    path('', views.voter, name='voter'),
    path('candidate/', views.candidate, name='candidate'),
]