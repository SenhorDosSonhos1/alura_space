from django.urls import path
from galeria import views

urlpatterns = [
    path('', views.index, name='index'),
    path('imagem/<int:id>', views.imagem, name='imagem'),
    path('buscar/', views.buscar, name='buscar')
]