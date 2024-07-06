from django.db import models

class Pemasukan(models.Model):
    tgl_pemasukan = models.DateField()
    pemasukan_gaji = models.CharField(max_length=100, unique=True)
    pendapatan_lainnya = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return str(self.tgl_pemasukan)  # Mengubah ke string untuk representasi objek yang benar

class Pengeluaran(models.Model):
    pemasukan = models.ForeignKey(Pemasukan, related_name="pengeluaran", on_delete=models.CASCADE)
    tgl_pengeluaran = models.CharField(max_length=100)
    belanja_bulanan = models.CharField(max_length=100, unique=True)
    tagihan = models.CharField(max_length=100, unique=True)
    pembelian_lainnya = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.tgl_pengeluaran

class LaporanKeuangan(models.Model):
    total_pemasukan = models.CharField(max_length=100)
    total_pengeluaran = models.CharField(max_length=100)
    saldo_akhir = models.CharField(max_length=100)

    def __str__(self):
        return self.total_pemasukan
