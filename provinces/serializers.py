from rest_framework import serializers
from .models import Province

class ProvinceSerializer(serializers.ModelSerializer):   
    class Meta:
        model = Province
        fields = ('id', 'province_name', 'province_state')
        read_only_field = ('id')
  