from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('links/', views.links, name='links'),
    path('gallery/', views.gallery, name='gallery'),
    path('gallery/<str:filter>', views.gallery_filter, name='gallery_filter'),
    path('add/', views.add, name='add'),
    path('photo/<str:pk>', views.photo, name='photo'),
    path('edit/<str:pk>', views.edit, name='edit'),
]