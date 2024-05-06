from django.db import models

class Pemasukan (models.Model):
    tgl_Pemasukan = models.CharField(max_length=100)
    pemasukan_gaji= models.CharField(max_length=10, unique=True)
    pendapatan_lainnya = models.CharField(max_length=10, unique=True)
    

    def __str__(self):
        return self.tgl_Pemasukan