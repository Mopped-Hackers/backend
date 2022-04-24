
from turtle import pu
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view

from ..serializers.purchase_serializer import PurchaseSerializer

from ..model.purchase import Purchase
import operator


@api_view(['POST'])
def getData(request):
    gameId = request.data.get('gameId')
    try:
        purchases = Purchase.objects.filter(gameId=gameId)
        ordered = sorted(purchases, key=operator.attrgetter('timestamp'))
        purchases = ordered
    except:
        purchases = None
        return HttpResponse("Internal error", status=500)
    if not purchases:
        return HttpResponse("No Content", status=204)
    serializer = PurchaseSerializer(purchases, many=True)
    return Response(serializer.data)