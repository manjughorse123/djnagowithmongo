from .models import *
from rest_framework import serializers


class DepastmentSerilaizer(serializers.ModelSerializer):
    

    class Meta:
        model = Depastment
        fields = '__all__'