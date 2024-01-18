from django.urls import path
from . import views

urlpatterns = [
    path('',views.home),
    path('registrarCurso/', views.registrarCursos,name='registrarCurso'),
    path('edicionCurso/<codigo>', views.edicionCurso),
    path('editarCurso/', views.editarCurso),
    path('eliminarCurso/<codigo>', views.eliminarCursos),
    
]