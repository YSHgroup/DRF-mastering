from rest_framework import serializers
from simple_crud.models import Tutorial

class TutorialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tutorial
        fields = '__all__' #field names to be included in the serialization - all