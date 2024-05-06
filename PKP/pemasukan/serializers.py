from rest_framework import serializers
from .models import Pemasukan

class PemasukanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pemasukan
        fields = '__all__'