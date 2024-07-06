from django.urls import path
from . import views

urlpatterns = [
    path('Pemasukan/', views.Pemasukan_list),
    path('Pemasukan/<int:pk>/', views.Pemasukan_detail),
    path('Pengeluaran/', views.PengeluaranList.as_view()),
    path('Pengeluaran/<int:pk>/', views.PengeluaranDetail.as_view()),
    path('Laporankeuangan/', views.Laporankeuangan_list),
    path('Laporankeuangan/<int:pk>/', views.Laporankeuangan_detail),
]
