from rest_framework import serializers
from .models import Pemasukan,Pengeluaran,Laporankeuangan

class PemasukanSerializer(serializers.ModelSerializer):
    Pengeluaran = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = Pemasukan
        fields = ["tgl_Pemasukan ", "pemasukan_gaji", "pendapatan_lainnya"]

class PengeluaranSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pengeluaran
        fields = ["tgl_Pengeluaran", "belanja_bulanan", "tagihan", "pembelian_lainnya"]

class LaporankeuanganSerializer(serializers.ModelSerializer):
    class Meta:
        model = Laporankeuangan
        fields = ["total_pemasukan", "total_pengeluaran", "saldo_akhir"]