from rest_framework.routers import DefaultRouter
from .views import RutinaViewSets, RutinaPersonalizadaViewSets, RutinaGetViewSets, RutinaPersonalizadaGetViewSets

router = DefaultRouter()
router.register('rutina-get', RutinaGetViewSets, basename='rutina-get-api')
router.register('rutinapersonalizada', RutinaPersonalizadaViewSets, basename='rutina-personalizada-api')
router.register('rutinapersonalizada-get', RutinaPersonalizadaGetViewSets, basename='rutina-personalizada-get-api')
router.register('', RutinaViewSets, basename='rutina-api')