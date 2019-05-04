from django.urls import path
from app_noticias.views import *

urlpatterns = [
    
    path('', HomePageView.as_view(), name='home'),
    path('post/<int:pk>/', detalhes, name='fullpost'),
    path('noticias/<int:noticia_id>', noticia_detalhes, name="detalhes"),
    path('noticias/resumo/', noticias_resumo, name='resumo'),
    path('noticias/resumo2/', noticias_resumo_template, name='resumo2'),
    path('noticias/tag/<str:pk>', slug_view, name='slug'),
    path('contato',ContatoView.as_view(),name='contato'),
    path('contato/sucesso',ContatoSucessoView.as_view(),name='contato_sucesso'),
] 

