import django_filters
from .models import Goods


class GoodsFilter(django_filters.rest_framework.FilterSet):
    '''商品过滤'''
    pricemin = django_filters.NumberFilter(field_name="shop_price", lookup_expr='gte', help_text='最小价格')
    pricemax = django_filters.NumberFilter(field_name="shop_price", lookup_expr='lte')

    class Meta:
        model = Goods
        fields = ['pricemin', 'pricemax','is_new','is_hot']
