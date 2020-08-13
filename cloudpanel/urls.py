
from django.urls import path

from . import views
from .views import ShopList, ShopDetail, CategoryList, CategoryDetail, ProductList, ProductDetail, ProductShopList, \
    FileUploadView

urlpatterns = [
    path('', views.index, name='index'),
    path('shoplist/<int:pk>', views.ListShops2.as_view(), name='shops'),
    # path('shoplist2/<int:pk>', views.ListShops2.as_view(), name='shops'),
    path('shops/', ShopList.as_view(), name='shop-list'),
    path('shops/<int:pk>', ShopDetail.as_view(), name='shop-detail'),
    path('category/', CategoryList.as_view(), name='category-list'),
    path('category/<int:pk>', CategoryDetail.as_view(), name='category-detail'),
    path('product/', ProductList.as_view(), name='product-list'),
    # path('productshop/<int:pk>', ProductShopList.as_view(), name='product-list'),
    path('product/<int:pk>', ProductDetail.as_view(), name='product-detail'),
    path('upload/', FileUploadView.as_view()),
]