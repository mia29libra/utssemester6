from rest_framework import serializers
from .models import Pemasukan,Pengeluaran, laporankeuangan

class PemasukanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pemasukan
        fields = '__all__'

class PengeluaranSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pengeluaran
        fields = '__all__'

class laporankeuanganSerializer(serializers.ModelSerializer):
    class Meta:
        model = laporankeuangan
        fields = '__all__'