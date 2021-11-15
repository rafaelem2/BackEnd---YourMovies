from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('api/favorite/', views.api_favorite),
    path('api/favoriteList/', views.api_favoriteList),
]
