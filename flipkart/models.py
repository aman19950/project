from django.db import models

# Create your models here.


class Registration(models.Model):
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    email = models.CharField(max_length=50, null=True, blank=True)
    pasword = models.CharField(max_length=255, null=True, blank=True)
    mobile = models.BigIntegerField(default=0)
    gender = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.first_name

# table for categories


class Category(models.Model):
    cat_name = models.CharField(
        max_length=100, default="", null=True, blank=True)
    cat_image = models.ImageField(upload_to='category/')

    def __str__(self):
        return self.cat_name

# table for products


class Product(models.Model):
    pro_name = models.CharField(
        max_length=100, default="", null=True, blank=True)
    pro_image = models.ImageField(upload_to='product/')
    price = models.IntegerField(null=True, blank=True, default=0)
    desc = models.TextField(max_length=255, default="", null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    @staticmethod
    def get_pro_for_cart(ids):
        return Product.objects.filter(id__in=ids)

    def __str__(self):
        return self.pro_name


class Order(models.Model):
    address = models.CharField(max_length=200, null=True, blank=True)
    mobile = models.BigIntegerField(default=0, null=True, blank=True)
    price = models.BigIntegerField(default=0, null=True, blank=True)
    customer = models.ForeignKey(Registration, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.BigIntegerField(default=0, null=True, blank=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.product.pro_name
