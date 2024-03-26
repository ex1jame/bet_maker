from django.urls import path
from .views import BetListApiView,BetCreateApiView,BetUpdateApiView

urlpatterns = [
    path('bets/', BetListApiView.as_view()),
    path('bets/create/', BetCreateApiView.as_view()),
    path('bets/<int:pk>/', BetUpdateApiView.as_view())
]