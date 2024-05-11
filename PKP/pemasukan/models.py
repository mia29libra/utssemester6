from django.db import models

class Pemasukan(models.Model):
    tgl_Pemasukan = models.CharField(max_length=100)
    pemasukan_gaji= models.CharField(max_length=10, unique=True)
    pendapatan_lainnya = models.CharField(max_length=10, unique=True)
    

    def __str__(self):
        return self.tgl_Pemasukan
    
class Pengeluaran(models.Model):
    Pemasukan = models.ForeignKey(Pemasukan, related_name="Pengeluaran", on_delete=models.CASCADE)
    tgl_Pengeluaran = models.CharField(max_length=100)
    belanja_bulanan= models.CharField(max_length=10, unique=True)
    tagihan = models.CharField(max_length=10, unique=True)
    pembelian_lainnya = models.CharField(max_length=10, unique=True)
    

    def __str__(self):
        return self.tgl_Pengeluaran
    
class Laporankeuangan(models.Model):
    total_pemasukan = models.CharField(max_length=100)
    total_pengeluaran= models.CharField(max_length=10, unique=True)
    saldo_akhir = models.CharField(max_length=10, unique=True)
    

    def __str__(self):
        return self.total_pemasukan