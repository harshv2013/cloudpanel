from rest_framework import serializers

from cloudpanel.models import Shop, Category, Product, Media


class ShopSerializer(serializers.ModelSerializer):

    class Meta:
        model = Shop
        # fields = ['shop_name', 'shop_location']
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        # fields = ['category_name', 'parent_cat']
        fields = "__all__"

class MediaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Media
        # fields = "__all__"
        fields = ['product_image','product']


class ProductSerializer(serializers.ModelSerializer):
    product_image = MediaSerializer(read_only=True)

    class Meta:
        model = Product
        # fields = "__all__"
        fields = ['product_name', 'category', 'product_image']
        # fields = ['product_name']

# class ProductShopSerializer(serializers.Serializer):
#     product_name = serializers.CharField(max_length=200)
#     category = CategorySerializer()
#     # shop = ShopSerializer(category)
#     id = serializers.IntegerField()




class ProductShopSerializer(serializers.ModelSerializer):
    # tests = ProductSerializer(read_only=True)
    # product  = ProductSerializer()
    # products = serializers.StringRelatedField(many=True)
    products = ProductSerializer(many=True)
    # media = MediaSerializer(many=True)

    class Meta:
        model = Category
        # fields = '__all__'
        fields = ('id', 'category_name', 'parent_cat', 'products')















# class ShopSerializer2(serializers.Serializer):
#     # product_name = serializers.CharField(max_length=200)
#     # category = CategorySerializer()
#     shop = ShopSerializer(CategorySerializer(ProductSerializer))
#     id = serializers.IntegerField()

class MediaSerializer2(serializers.ModelSerializer):

    class Meta:
        model = Media
        # fields = "__all__"
        fields = ['product_image']

class ProductSerializer2(serializers.ModelSerializer):
    media = MediaSerializer2(many=True)

    class Meta:
        model = Product
        # fields = "__all__"
        fields = ['product_name', 'category','media']
        fields = ['product_name', 'media']
        # fields = ['product_name']

class ProductShopSerializer2(serializers.ModelSerializer):
    # # product_name = serializers.CharField(max_length=200)
    # # category_name = serializers.CharField(max_length=200)
    # # shop = ShopSerializer(CategorySerializer(ProductSerializer()))
    # category = CategorySerializer(ProductSerializer())
    # # product = ProductSerializer()
    # # shop = ShopSerializer(category)
    # id = serializers.IntegerField()

    product = ProductSerializer2(many=True)
    # media = MediaSerializer(many=True)

    class Meta:
        model = Category
        # fields = '__all__'
        fields = ('id', 'category_name', 'parent_cat','product')
        # fields = ['product_name', 'category']










