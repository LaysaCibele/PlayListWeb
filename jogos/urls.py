from django.urls import path
from . import views

urlpatterns = [
    path('detalhes/<int:id_do_jogo>/', views.pagina_do_jogo, name='pagina_do_jogo'),
]