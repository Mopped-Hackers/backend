
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view

from ..serializers.purchase_serializer import PurchaseSerializer

from ..model.purchase import Purchase

@api_view(['GET'])
def getData(request):
    try:
        purchases = Purchase.objects.all().order_by('-id')
    except:
        purchases = None
    if not purchases:
        return HttpResponse("No Content", status=404)
    serializer = PurchaseSerializer(purchases, many=True)
    return Response(serializer.data)