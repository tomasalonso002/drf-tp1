from rest_framework.routers import DefaultRouter
from .views import RutinaViewSets, RutinaPersonalizadaViewSets

router = DefaultRouter()
router.register('rutina', RutinaViewSets, basename='rutina-api')
router.register('rutinapersonalizada', RutinaPersonalizadaViewSets, basename='rutinapersonalizada-api')
