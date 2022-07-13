from django.urls import path
from .views import *
from . import views
urlpatterns = [
    path('obras/lista/Geral/', Lista_Geral_Obras.as_view(), name='Lista_Geral_Obras'),
    path('obras/lista/Atribuidas/', Lista_Geral_Atribuidas_Obras.as_view(), name='Lista_Geral_Atribuidas_Obras'),
    path('obras/lista/N_Atribuidas/', Lista_Geral_N_Atribuidas_Obras.as_view(), name='Lista_Geral_N_Atribuidas_Obras'),
    path('obras/lista/Analista/', Lista_Geral_Analista_Obras.as_view(), name='Lista_Geral_Analista_Obras'),
    path('obras/proposta/<str:pk>/', Detalha_Proposta_Obras.as_view(), name='Detalha_Proposta_Obras'),
    path('obras/lista/<str:slug>/', views.Filtros_Lista_Obras, name='Filtros_Lista_Obras'),

    path('equipamentos/lista/Geral/', Lista_Geral_Equipamentos.as_view(), name='Lista_Geral_Equipamentos'),
    path('equipamentos/lista/Atribuidas/', Lista_Geral_Atribuidas_Equipamentos.as_view(), name='Lista_Geral_Atribuidas_Equipamentos'),
    path('equipamentos/lista/N_Atribuidas/', Lista_Geral_N_Atribuidas_Equipamentos.as_view(), name='Lista_Geral_N_Atribuidas_Equipamentos'),
    path('equipamentos/lista/Analista/', Lista_Geral_Analista_Equipamentos.as_view(), name='Lista_Geral_Analista_Equipamentos'),
    path('equipamentos/proposta/<str:pk>/', Detalha_Proposta_Equipamentos.as_view(), name='Detalha_Proposta_Equipamentos'),
    path('equipamentos/lista/<str:slug>/', views.Filtros_Lista_Equipamentos, name='Filtros_Lista_Equipamentos'),

    path('fatos/<str:pk>/', views.fatos_geradores, name='reg_fatos_geradores'),
    path('notificacao/<str:pk>/', views.reg_notificacao, name='reg_notificacao'),
    path('edital/<str:pk>/', views.reg_edital_notif, name='reg_edital_notif'),
    path('restituicao/<str:pk>/', views.reg_restituicao, name='reg_restituicao'),
    path('valores/<str:pk>/', views.reg_valores, name='reg_valores'),
    path('acompanhamento/<str:pk>/', views.reg_acompanhamento, name='reg_acompanhamento'),

]