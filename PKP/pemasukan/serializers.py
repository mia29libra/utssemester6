from rest_framework import serializers
from .models import Pemasukan,Pengeluaran

class PemasukanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pemasukan
        fields = '__all__'

class PengeluaranSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pengeluaran
        fields = '__all__'