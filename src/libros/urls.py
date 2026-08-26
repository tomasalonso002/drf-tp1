from django.urls import path
from .views import libros, libros_detail
urlpatterns = [
    path('', libros, name='libros-api'),
    path('<int:pk>/',libros_detail, name='libros-api-detail')
]