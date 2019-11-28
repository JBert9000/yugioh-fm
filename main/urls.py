from django.urls import path
from . import views
from .views import (
    HomePageView,

)


urlpatterns = [
    # path('', views.home, name='main-home'),
    path('', HomePageView.as_view(), name='main-home'),
    path('guide/', views.guide, name='main-guide'),
    path('streams/', views.streams, name='main-streams'),
]
