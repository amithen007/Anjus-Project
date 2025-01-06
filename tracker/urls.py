from django.urls import path
from . import views

urlpatterns = [
    path('track/', views.track_user, name='track_user'),
]
