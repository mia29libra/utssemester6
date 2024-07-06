from rest_framework import status, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.http import Http404
from rest_framework.views import APIView
from .models import Pemasukan, Pengeluaran, LaporanKeuangan  # Ubah Laporankeuangan menjadi LaporanKeuangan
from .serializers import PemasukanSerializer, PengeluaranSerializer, LaporanKeuanganSerializer  # Ubah LaporankeuanganSerializer menjadi LaporanKeuanganSerializer

# Create your views here.
@api_view(['GET', 'POST'])
@permission_classes([permissions.AllowAny])
def Pemasukan_list(request, format=None):
    if request.method == 'GET':
        pemasukan = Pemasukan.objects.all()
        serializer = PemasukanSerializer(pemasukan, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PemasukanSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def Pemasukan_detail(request, pk, format=None):
    try:
        pemasukan = Pemasukan.objects.get(pk=pk)
    except Pemasukan.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PemasukanSerializer(pemasukan)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = PemasukanSerializer(pemasukan, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        pemasukan.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class PengeluaranList(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, format=None):
        pengeluaran = Pengeluaran.objects.all()
        serializer = PengeluaranSerializer(pengeluaran, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = PengeluaranSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PengeluaranDetail(APIView):
    permission_classes = [permissions.AllowAny]

    def get_object(self, pk):
        try:
            return Pengeluaran.objects.get(pk=pk)
        except Pengeluaran.DoesNotExist:
            raise Http404
        
    def get(self, request, pk, format=None):
        pengeluaran = self.get_object(pk)
        serializer = PengeluaranSerializer(pengeluaran)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        pengeluaran = self.get_object(pk)
        serializer = PengeluaranSerializer(pengeluaran, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        pengeluaran = self.get_object(pk=pk)
        pengeluaran.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
@permission_classes([permissions.AllowAny])
def Laporankeuangan_list(request, format=None):
    if request.method == 'GET':
        laporankeuangan = LaporanKeuangan.objects.all()  # Menggunakan LaporanKeuangan sesuai dengan definisi model
        serializer = LaporanKeuanganSerializer(laporankeuangan, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = LaporanKeuanganSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def Laporankeuangan_detail(request, pk, format=None):
    try:
        laporankeuangan = LaporanKeuangan.objects.get(pk=pk)  # Menggunakan LaporanKeuangan sesuai dengan definisi model
    except LaporanKeuangan.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = LaporanKeuanganSerializer(laporankeuangan)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = LaporanKeuanganSerializer(laporankeuangan, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        laporankeuangan.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
