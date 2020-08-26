from django.urls import path
from . import views

urlpatterns = [
    path('display_funds/', views.view_display_funds, name='display_funds'),
]