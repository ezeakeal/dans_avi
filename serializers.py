from rest_framework import serializers
from avi.models import DemoModel

class DemoModelSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = DemoModel
        fields = ('id', 'query', 'outputFile')
