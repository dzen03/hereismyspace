from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('links/', views.links, name='links'),
    path('gallery_old/', views.gallery_old, name='gallery'),
    path('gallery_old/<str:filter>', views.gallery_filter_old, name='gallery_filter'),
    path('add/', views.add, name='add'),
    path('photo/<str:pk>', views.photo, name='photo'),
    path('edit/<str:pk>', views.edit, name='edit'),

    path('gallery/<str:pk>', views.gallery_filter, name='gallery_filter_new'),
    path('gallery/', views.gallery, name='gallery_new'),
]