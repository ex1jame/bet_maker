from rest_framework import serializers
from .models import Bets

class BetListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bets
        fields = ('id', 'amount', 'status')

class BetCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bets
        fields = '__all__'

class BetUpdateSerializer(serializers.ModelSerializer):
    # new_status = serializers.ChoiceField(choices=('WIN', 'LOST'))
    class Meta:
        model = Bets
        fields = ('id','status')