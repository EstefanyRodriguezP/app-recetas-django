from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='inicio'),  # esta es la página en /
    path('recetas/', views.recetas, name='recetas'),  # esta también responde en /inicio/
    path('recetas/<int:receta_id>/', views.receta_detalle, name='receta_detalle'),  # Detalle de receta
    path('contacto/', views.contacto, name='contacto'),
    path('mensaje-enviado/', views.mensaje_enviado, name='mensaje_enviado'),
]

