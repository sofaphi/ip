from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('gallery/', views.Gallery.as_view(), name='gallery'),
    path('gallery/<pk>/', views.AchievementItem.as_view(), name='gallery-item'),
]
