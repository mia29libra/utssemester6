from rest_framework import serializers
from .models import Pemasukan, Pengeluaran, LaporanKeuangan  # Ubah Laporankeuangan menjadi LaporanKeuangan

class PemasukanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pemasukan
        fields = ["id","tgl_pemasukan", "pemasukan_gaji", "pendapatan_lainnya"]

class PengeluaranSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pengeluaran
        fields = ["tgl_pengeluaran", "belanja_bulanan", "tagihan", "pembelian_lainnya"]

class LaporanKeuanganSerializer(serializers.ModelSerializer):
    class Meta:
        model = LaporanKeuangan
        fields = ["total_pemasukan", "total_pengeluaran", "saldo_akhir"]
