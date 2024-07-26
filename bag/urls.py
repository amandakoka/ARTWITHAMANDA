from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_bag, name='view_bag'),
    path('add_to_bag/<int:artwork_id>/', views.add_to_bag, name='add_to_bag'),
    path('adjust/<int:artwork_id>/', views.adjust_bag, name='adjust_bag'),
    path('remove/<artwork_id>/', views.remove_from_bag, name='remove_from_bag'),
]
