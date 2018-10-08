from rest_framework.views import APIView
from goods.serializers import GoodsSerializer,CategorySerializer
from .models import Goods,GoodsCategory
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from .filters import GoodsFilter
from rest_framework import filters

# Create your views here.

class GoodsPagination(PageNumberPagination):
    '''商品分页'''
    page_size = 10
    page_size_query_param = 'page_size'
    page_query_param = 'page'
    max_page_size = 100


# class GoodsListView(APIView):
#     '''
#     商品列表
#     '''
#     def get(self, request, format=None):
#         goods = Goods.objects.all()
#         goods_serializer = GoodsSerializer(goods,many=True)
#         return Response(goods_serializer.data)


# class GoodsListView(generics.ListAPIView):
#     '''商品列表'''
#     queryset = Goods.objects.all()
#     serializer_class = GoodsSerializer


class GoodsListViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    '''商品列表'''

    # 这里必须要定义一个默认的排序,否则会报错
    queryset = Goods.objects.all().order_by('id')
    # 分页
    pagination_class = GoodsPagination
    serializer_class = GoodsSerializer
    # filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)

    # 设置filter的类为我们自定义的类
    filter_class = GoodsFilter
    search_fields = ('name', 'goods_brief', 'goods_desc')
    ordering_fields = ('sold_num', 'shop_price')


class CategoryViewSet(mixins.ListModelMixin,mixins.RetrieveModelMixin,viewsets.GenericViewSet):
    '''
    商品分类表数据
    '''
    queryset = GoodsCategory.objects.filter(category_type=1)
    serializer_class = CategorySerializer


