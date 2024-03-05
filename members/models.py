from django.db import models
class Account_details(models.Model):
    firstname=models.CharField(max_length=30,null=True)
    lastname=models.CharField(max_length=30,null=True)
    email = models.EmailField(max_length=50,null=True)
    password = models.CharField(max_length=8,null=True)
    phone=models.CharField(max_length=10,null=True)

class Products(models.Model):
    name=models.CharField(max_length=50,null=True)
    desc=models.CharField(max_length=150,null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2,null=True)

class Brand(models.Model):
    name=models.CharField(max_length=50,null=True)
class Category(models.Model):
    name=models.CharField(max_length=50,null=True)
class Orders(models.Model):
    date = models.DateField(null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2, null=True)
class Order_items(models.Model):
    quantity = models.IntegerField(null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
class Accessories(models.Model):
    name=models.CharField(max_length=50,null=True)
    desc=models.CharField(max_length=150,null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2,null=True)