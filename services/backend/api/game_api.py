
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view

from ..model.game import Game
from ..serializers.game_serializers import GameSerializer


@api_view(['GET'])
def gameList(request):
    try:
        places = Game.objects.all().order_by('-id')
    except:
        places = None
    if not places:
        return HttpResponse("No Content", status=404)
    serializer = GameSerializer(places, many=True)
    return Response(serializer.data)
