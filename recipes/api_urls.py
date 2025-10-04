from django.urls import path
from . import views_api

urlpatterns = [
    path('recipes/', views_api.recipe_list_create, name='recipe_list_create'),
    path('recipes/<int:pk>/', views_api.recipe_detail, name='recipe_detail'),
]
