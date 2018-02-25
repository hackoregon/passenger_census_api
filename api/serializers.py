from rest_framework import serializers
from api.models import PassengerCensus

class PassengerCensusSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = PassengerCensus
        fields = '__all__'