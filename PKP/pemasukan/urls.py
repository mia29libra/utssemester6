from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PemasukanViewSet, PengeluaranViewSet

router = DefaultRouter()
router.register(r'pemasukan', PemasukanViewSet)
router.register(r'pengeluaran', PengeluaranViewSet)

urlpatterns = router.urls