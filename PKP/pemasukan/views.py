from rest_framework import viewsets
from .models import Pemasukan
from .serializers import PemasukanSerializer

class PemasukanViewSet(viewsets.ModelViewSet):
    queryset = Pemasukan.objects.all()
    serializer_class = PemasukanSerializer
