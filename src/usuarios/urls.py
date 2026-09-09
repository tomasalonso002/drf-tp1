from django.urls import path

from .views import UserListCreateView,UserRetrivUpdateView,UsuarioSoftDeleteView

urlpatterns = [
    path("", UserListCreateView.as_view(), name="usuario_api"),
    path("<int:pk>/", UserRetrivUpdateView.as_view(), name="detail_usuario_api"),
    path("<int:pk>/desactivar/", UsuarioSoftDeleteView.as_view(), name="desactivar_usuario_api"),
]