from django.shortcuts import render
from rest_framework import generics
from .models import Bets
from .serializers import BetListSerializer,BetUpdateSerializer,BetCreateSerializer
# Create your views here.
class BetListApiView(generics.ListAPIView):
    queryset = Bets.objects.all()
    serializer_class = BetListSerializer

class BetCreateApiView(generics.ListCreateAPIView):
    queryset = Bets.objects.all()
    serializer_class = BetCreateSerializer

class BetUpdateApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bets.objects.all()
    serializer_class = BetUpdateSerializer

