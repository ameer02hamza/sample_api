from rest_framework import serializers
from .models import *


class timeSheetSerializer(serializers.ModelSerializer):
    class Meta:
        model = timeSheet
        fields = '__all__'


class pileLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = pileLogs
        fields = '__all__'
