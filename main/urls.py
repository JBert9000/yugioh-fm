from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='main-home'),
    path('guide/', views.guide, name='main-guide'),
    path('streams/', views.streams, name='main-streams'),
]
