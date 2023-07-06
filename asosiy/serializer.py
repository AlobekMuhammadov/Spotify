from .models import *
from rest_framework.serializers import Serializer,ModelSerializer

class QoshiqchiSerializer(ModelSerializer):
    class Meta:
        model = Qoshiqchi
        fields = '__all__'

class AlbomSerializer(ModelSerializer):
    class Meta:
        model = Albom
        fields= '__all__'

class QoshiqSerializer(ModelSerializer):
    class Meta:
        model = Qoshiq
        fields = '__all__'


