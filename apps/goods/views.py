from rest_framework.views import APIView
from goods.serializers import GoodsSerializer
from .models import Goods
from rest_framework.response import Response
# Create your views here.





class GoodsListView(APIView):
    '''
    商品列表
    '''
    def get(self, request, format=None):
        goods = Goods.objects.all()
        goods_serializer = GoodsSerializer(goods,many=True)
        return Response(goods_serializer.data)
