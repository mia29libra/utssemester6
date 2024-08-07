# Generated by Django 5.0.4 on 2024-07-06 00:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LaporanKeuangan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_pemasukan', models.CharField(max_length=100)),
                ('total_pengeluaran', models.CharField(max_length=100)),
                ('saldo_akhir', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Pemasukan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tgl_pemasukan', models.DateField()),
                ('pemasukan_gaji', models.CharField(max_length=100, unique=True)),
                ('pendapatan_lainnya', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Pengeluaran',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tgl_pengeluaran', models.CharField(max_length=100)),
                ('belanja_bulanan', models.CharField(max_length=100, unique=True)),
                ('tagihan', models.CharField(max_length=100, unique=True)),
                ('pembelian_lainnya', models.CharField(max_length=100, unique=True)),
                ('pemasukan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pengeluaran', to='pemasukan.pemasukan')),
            ],
        ),
    ]
