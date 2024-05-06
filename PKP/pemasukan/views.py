from rest_framework import viewsets
from .models import Pemasukan, Pengeluaran, laporankeuangan
from .serializers import PemasukanSerializer, PengeluaranSerializer, laporankeuanganSerializer

class PemasukanViewSet(viewsets.ModelViewSet):
    queryset = Pemasukan.objects.all()
    serializer_class = PemasukanSerializer

class PengeluaranViewSet(viewsets.ModelViewSet):
    queryset = Pengeluaran.objects.all()
    serializer_class = PengeluaranSerializer

class laporankeuanganViewSet(viewsets.ModelViewSet):
    queryset = laporankeuangan.objects.all()
    serializer_class = laporankeuanganSerializer
