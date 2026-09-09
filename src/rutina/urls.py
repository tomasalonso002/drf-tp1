from django.urls import path

from .views import RutinaListCreateView,RutinaPersonalizadaListCreateView,RutinaDetailApiView,RutinaPersonalizadaDetailApiView

urlpatterns = [
    path("", RutinaListCreateView.as_view(), name="rutina_api"),
    path("<int:pk>/",RutinaDetailApiView.as_view(), name="rutina_detail_api"),
    path("rutinapersonalizada/<int:pk>/", RutinaPersonalizadaDetailApiView.as_view(), name='rutina_personalizada_detail_api'),
    path("rutinapersonalizada/", RutinaPersonalizadaListCreateView.as_view(), name="rutina_personalizada_api"),
]