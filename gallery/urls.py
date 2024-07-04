from django.urls import path
from . import views

urlpatterns = [
    path('', views.gallery, name='gallery'),
    path('review/', views.review_form, name='review_form'),
]
