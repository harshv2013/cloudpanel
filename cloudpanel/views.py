import json

from django.http import HttpResponse, Http404
from rest_framework import status
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView
from cloudpanel.models import Shop, Category, Product, Media
from cloudpanel.serializers import ShopSerializer, CategorySerializer, ProductSerializer, ProductShopSerializer, \
    ProductShopSerializer2, MediaSerializer


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")



class ListShops(APIView):

    # def get(self, request, pk, format=None):
    #     """
    #     Return a list of all users.
    #     """
    #     shops = [shop.shop_name for shop in Shop.objects.all()]
    #     return Response(shops)


    def get(self, request,pk, format=None):
        # product = Product.objects.filter(category__shop__id=pk)
        # serializer = ProductShopSerializer(product, many=True)
        category = Category.objects.filter(shop=pk)
        print('category ----------------',category)
        serializer = ProductShopSerializer(category, many=True)
        return Response(serializer.data)
        # return HttpResponse(json.dumps({'name':'HK'}))

########################################################################
class ListShops2(APIView):

    # def get(self, request, format=None):
    #     """
    #     Return a list of all users.
    #     """
    #     shops = [shop.shop_name for shop in Shop.objects.all()]
    #     return Response(shops)
    def get(self, request,pk, format=None):
        # shop = Shop.objects.filter(id=pk)
        # product = Product.objects.filter(category__shop=pk)
        category = Category.objects.filter(shop__id=pk)
        # product = Product.objects.filter(category__shop__id=pk)
        # print('product fetched----------',product)
        # print('category object ----------',[c.product for c in category])
        serializer = ProductShopSerializer2(category, many=True)
        print('serilizer data is ---------', serializer.data)
        return Response(serializer.data)
        # return Response({'name':'HK'})
        # return HttpResponse(json.dumps({'name':'HK'}))



########################################################################

class ShopList(APIView):
    """
    List all Shop, or create a new shop.
    """
    def get(self, request, format=None):
        shops = Shop.objects.all()
        serializer = ShopSerializer(shops, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ShopSerializer(data=request.data)
        # print('serializer -s ---',serializer.data)
        print('data ----', request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ShopDetail(APIView):

    """
    Retrieve, update or delete a ScheduleClass instance.
    """
    def get_object(self, pk):
        try:
            return Shop.objects.get(pk=pk)
        except Shop.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        shop = self.get_object(pk)
        serializer = ShopSerializer(shop)
        return Response(serializer.data)


    def put(self, request, pk, format=None):
        shop = self.get_object(pk)
        serializer = ShopSerializer(shop, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        shop = self.get_object(pk)
        shop.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

########################################################################

class CategoryList(APIView):
    """
    List all Shop, or create a new shop.
    """
    def get(self, request, format=None):
        catogery = Category.objects.all()
        serializer = CategorySerializer(catogery, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CategorySerializer(data=request.data)
        # print('serializer -s ---',serializer.data)
        print('data ----', request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CategoryDetail(APIView):

    """
    Retrieve, update or delete a ScheduleClass instance.
    """
    def get_object(self, pk):
        try:
            return Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        category = self.get_object(pk)
        serializer = CategorySerializer(category)
        return Response(serializer.data)


    def put(self, request, pk, format=None):
        category = self.get_object(pk)
        serializer = CategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400shop_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        category = self.get_object(pk)
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




########################################################################

class ProductList(APIView):
    """
    List all Shop, or create a new shop.
    """
    def get(self, request, format=None):
        # product = Product.objects.filter(category__shop=pk).all()
        # print('product are************************', product)
        product = Product.objects.all()
        serializer = ProductSerializer(product, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ProductSerializer(data=request.data)
        # print('serializer -s ---',serializer.data)
        print('data ----', request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductShopList(APIView):
    """
    List all Shop, or create a new shop.
    """
    def get(self, request, pk, format=None):
        # product = Product.objects.filter(category__shop=pk).all()
        # print('product are************************', product)
        product = Product.objects.filter(category__shop=pk).all()
        serializer = ProductShopSerializer(product, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ProductSerializer(data=request.data)
        # print('serializer -s ---',serializer.data)
        print('data ----', request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductDetail(APIView):

    """
    Retrieve, update or delete a ScheduleClass instance.
    """
    def get_object(self, pk):
        try:
            # return Product.objects.filter(category__shop_id=pk).all()
            return Product.objects.get(pk=pk)

        except Product.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        # print('pk is -----------------',pk)
        # product = Product.objects.filter(category__shop=pk).all()
        product = self.get_object(pk)
        print('products are ----------------------------------------------', product)
        serializer = ProductSerializer(product)
        return Response(serializer.data)


    def put(self, request, pk, format=None):
        product = self.get_object(pk)
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400shop_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        category = self.get_object(pk)
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class FileUploadView(APIView):
    parser_class = (FileUploadParser,)

    def post(self, request, *args, **kwargs):

      file_serializer = MediaSerializer(data=request.data)

      if file_serializer.is_valid():
          file_serializer.save()
          return Response(file_serializer.data, status=status.HTTP_201_CREATED)
      else:
          return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, *args, **kwargs):
        media = Media.objects.all()
        serilizer = MediaSerializer(media,many=True)
        return Response(serilizer.data)


