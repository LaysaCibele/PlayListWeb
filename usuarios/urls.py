from django.urls import path
from usuarios import views

urlpatterns = [
    path('login/', views.login_page, name='login'),
    path('cadastro/', views.cadastro_page, name='cadastro'),
]