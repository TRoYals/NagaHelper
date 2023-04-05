from rest_framework import serializers
from .models import NagaData,NagaName

class NagaDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = NagaData
        fields = ('id', 'title', 'description', 'date','creater')

class NagaNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = NagaName
        fields = ('id', 'title', 'rest')