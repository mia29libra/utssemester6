from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PemasukanViewSet, PengeluaranViewSet, laporankeuanganViewSet

router = DefaultRouter()
router.register(r'pemasukan', PemasukanViewSet)
router.register(r'pengeluaran', PengeluaranViewSet)
router.register(r'laporankeuangan', laporankeuanganViewSet)

urlpatterns = router.urls