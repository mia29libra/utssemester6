from rest_framework import viewsets
from .models import Pemasukan, Pengeluaran
from .serializers import PemasukanSerializer, PengeluaranSerializer

class PemasukanViewSet(viewsets.ModelViewSet):
    queryset = Pemasukan.objects.all()
    serializer_class = PemasukanSerializer

class PengeluaranViewSet(viewsets.ModelViewSet):
    queryset = Pengeluaran.objects.all()
    serializer_class = PengeluaranSerializer
