from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('cadastroFarmacia/', views.cadastroFarmacia, name='cadastroFarmacia'),
    path('cadastro-produto/', views.cadastroProduto, name='cadastro-produto'),    
    path('produtos/', views.produtos, name='produtos'),    
    path('detalhes/<int:id>', views.detalhes, name='detalhes'),  
]
