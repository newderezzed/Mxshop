"""MXshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
import xadmin
from django.urls import path, include, re_path
from django.views.static import serve
from MXshop.settings import MEDIA_ROOT
# from goods.view_base import GoodsListView
from goods.views import GoodsListViewSet, CategoryViewSet, BannerViewset, IndexCategoryViewset
from user_operation.views import UserFavViewset, LeavingMessageViewset, AddressViewset
from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter
# from rest_framework.authtoken import views
from rest_framework_jwt.views import obtain_jwt_token
from users.views import SmsCodeViewset, UserViewset
from trade.views import ShoppingCartViewset, OrderViewset
router = DefaultRouter()

router.register(r'goods', GoodsListViewSet, base_name='goods')
router.register(r'categorys', CategoryViewSet, base_name='categorys')
router.register(r'code', SmsCodeViewset, base_name='code')
router.register(r'users', UserViewset, base_name="users")
router.register(r'userfavs', UserFavViewset, base_name="userfavs")
router.register(r'message', LeavingMessageViewset, base_name='message')
router.register(r'address', AddressViewset, base_name="address")
router.register(r'shopcarts', ShoppingCartViewset, base_name="shopcarts")
router.register(r'orders', OrderViewset, base_name="orders")
router.register(r'banners', BannerViewset, base_name="banners")
router.register(r'indexgoods', IndexCategoryViewset, base_name="indexgoods")

urlpatterns = [
    path('xadmin/', xadmin.site.urls),
    path('ueditor/', include('DjangoUeditor.urls')),
    path('media/<path:path>', serve, {'document_root': MEDIA_ROOT}),
    # path('goods/',GoodsListView.as_view(),name='goods-list'),
    path('docs', include_docs_urls(title='仙剑奇侠传')),
    path('api-auth/', include('rest_framework.urls')),
    # path('api-token-auth/',views.obtain_auth_token),  # token
    path('login/', obtain_jwt_token),
    re_path('^', include(router.urls))
]
