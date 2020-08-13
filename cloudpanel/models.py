
from django.db import models


class Shop(models.Model):
    shop_name = models.CharField(max_length=200)
    shop_location = models.CharField(max_length=200)

    # def __str__(self):
    #     return self.shop_name


class Category(models.Model):
    category_name = models.CharField(max_length=200)
    parent_cat = models.IntegerField(blank=True, null=True, default=None)
    shop = models.ForeignKey(Shop, related_name='category', on_delete=models.CASCADE)

    # def __str__(self):
    #     return self.category_name


class Product(models.Model):
    product_name = models.CharField(max_length=200)
    category = models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE)

    # def __str__(self):
    #     return self.product_name

class Media(models.Model):
    product_image = models.ImageField(null=True)
    product = models.ForeignKey(Product, related_name='media', on_delete=models.CASCADE)

############################################################################

class Reporter(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)

class Article(models.Model):
    headline = models.CharField(max_length=100)
    pub_date = models.DateField()
    reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)

    def __str__(self):
        return self.headline

    class Meta:
        ordering = ['headline']


