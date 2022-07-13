from django.contrib.auth import views as auth_views
from django.urls import path
from .views import *
from . import views
urlpatterns = [
    path('', Home.as_view(), name="home"),
    path('account/registro/', register, name="registro"),
    path('account/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('account/login/', auth_views.LoginView.as_view(template_name='account/login.html'), name="login"),
    path('account/senha/', views.altera_senha, name='altera_senha'),
    path('account/lista/', UserList.as_view(), name='UserList'),
    path('account/update/<int:pk>/', UserUpdate.as_view(), name='UserUpdate'),
    path('account/usuario_update/<int:pk>/', UsuarioUpdate.as_view(), name='UsuarioUpdate'),
]