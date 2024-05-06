from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PemasukanViewSet

router = DefaultRouter()
router.register(r'pemasukan', PemasukanViewSet)

urlpatterns = [
    path('pemasukan/', include(router.urls)),
]
