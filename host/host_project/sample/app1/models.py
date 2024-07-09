from django.db import models

# Create your models here.
class user_register(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField()
    phno=models.IntegerField()
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=20)

class product(models.Model):
    cake_name=models.CharField(max_length=20)
    cake_price=models.IntegerField()
    cake_stock=models.IntegerField()
    cake_img=models.ImageField()

class cart(models.Model):
    user_details=models.ForeignKey(user_register,on_delete=models.CASCADE)
    product_details=models.ForeignKey(product,on_delete=models.CASCADE)
    quantity=models.IntegerField(default=1)
    total_price=models.IntegerField(null=True)

class wishlist(models.Model):
    user_details=models.ForeignKey(user_register,on_delete=models.CASCADE)
    product_details=models.ForeignKey(product,on_delete=models.CASCADE)

