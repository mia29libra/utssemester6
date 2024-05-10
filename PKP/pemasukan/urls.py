from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('Pemasukan/', views.Pemasukan_list),
    path('Pemasukan/<int:pk>/', views.Pemasukan_detail),
    path('Pengeluaran/', views.PengeluaranList.as_view()),
    path('Pengeluaran/<int:pk>/', views.PengeluaranDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)