from django.urls import path
from . import views

urlpatterns = [
    path('display_pea/', views.view_display_pea, name='display_pea'),
    path('register_pea/', views.view_register_new_pea.as_view(), name='register_pea'),
    path('register_order_funds/', views.view_register_new_order_funds.as_view(), name='register_order_funds'),
    path('register_order_assets/', views.view_register_new_order_asset.as_view(), name='register_order_assets'),
    path('display_pea/<str:name_pea>/', views.view_display_one_pea, name='display_one_pea'),
]