from django.urls import path
from listas import views

urlpatterns = [
    path('biblioteca/', views.biblioteca_view, name='biblioteca'),
]