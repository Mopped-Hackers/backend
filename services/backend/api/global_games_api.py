from rest_framework.decorators import api_view
from ..model.game import Game
from ..serializers.game_serializers import GameSerializer
from django.http import HttpResponse
from rest_framework.response import Response

@api_view(['GET'])
def getGlobalDataTop(request):
    games = Game.objects.all().order_by('-rank')[:5] 
    serializer = GameSerializer(games, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getGlobalDataBottom(request):
    games = Game.objects.all().order_by('-rank').reverse()[:5] 
    serializer = GameSerializer(games, many=True)
    return Response(serializer.data)

