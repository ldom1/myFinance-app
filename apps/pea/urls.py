from django.urls import path
from . import views

urlpatterns = [
    path('display_pea/', views.view_display_pea, name='display_pea'),
    path('register_pea/', views.view_register_new_pea.as_view(), name='register_pea'),
    path('register_order/', views.view_register_new_order.as_view(), name='register_order'),
    path('display_pea/<str:name_pea>/', views.view_display_one_pea, name='display_one_pea'),
]