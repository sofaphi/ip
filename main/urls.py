from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('gallery/', views.Gallery.as_view(), name='gallery'),
    path('gallery/<pk>/', views.AchievementItem.as_view(), name='gallery-item'),
    path('achievement-create/', views.AchievementCreate.as_view(), name='achievement-create'),
    path('achievement-delete/<pk>/', views.DeleteAchievement.as_view(), name="achievement-delete"),
    path('achievement-change/<pk>/', views.ChangeAchievement.as_view(), name="achievement-change"),
]
