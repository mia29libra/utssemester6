from rest_framework import status, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.http import Http404
from rest_framework.views import APIView
from .models import Pemasukan, Pengeluaran
from .serializers import PemasukanSerializer, PengeluaranSerializer

# Create your views here.
@api_view(['GET', 'POST']) # decorator
@permission_classes([permissions.AllowAny])
def Pemasukan_list(request, format=None):

    if request.method == 'GET':
        Pemasukan = Pemasukan.objects.all()
        serializer = PemasukanSerializer(Pemasukan, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PemasukanSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def Pemasukan_detail(request, pk, format=None):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        kategori = Pemasukan.objects.get(pk=pk)
    except Pemasukan.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PemasukanSerializer(kategori)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = PemasukanSerializer(kategori, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        kategori.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# view untuk produk dengan class base view
class PengeluaranList(APIView):
    """
    ini merupakan proses pengambilan data atau simpan data
    """
    permission_classes = [permissions.AllowAny]
    def get(self, request, format=None):
        produk = Pengeluaran.objects.all()
        serializer = PengeluaranSerializer(produk, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = PengeluaranSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProdukDetail(APIView):
    """
    ambil data, edit atau hapus data
    """
    parser_classes = [permissions.AllowAny]
    def get_object(self, pk):
        try:
            return Pengeluaran.objects.get(pk=pk)
        except Pengeluaran.DoesNotExist:
            raise Http404
        
    def get(self, request, pk, format=None):
        produk = self.get_object(pk)
        serializer = PengeluaranSerializer(produk)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        produk = self.get_object(pk)
        serializer = PengeluaranSerializer(produk, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        produk = self.get_object(pk=pk)
        produk.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)