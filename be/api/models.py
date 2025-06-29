from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.hashers import make_password, check_password
# Create your models here.

#role_id
class Role(models.Model):
    name =models.CharField(max_length=50,unique = True)

    def __str__(self):
        return self.name


#check user
class CustomUser(AbstractUser):
   username = models.CharField(max_length=100,unique = True,blank= False)
   email = models.EmailField(unique=True)
   password = models.CharField(max_length=255)
   role = models.ForeignKey(Role,on_delete=models.SET_NULL,null = True)
   is_active = models.BooleanField(default=True)
   def set_password(self, raw_password):
       self.password = make_password(raw_password)
   def check_password(self, raw_password):
       return check_password(raw_password,self.password)
   def __str__(self):
       return self.username


# product
class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10,decimal_places=2)
    image = models.URLField()
    stock = models.IntegerField()
    def __str__(self):
        return self.name
   
#cart
class Cart(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    product =models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.IntegerField(default = 1)


    def __str__(self):
        return f"Cart: {self.user.username} - {self.product.name}"

#order    
class Order(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('shipped', 'Shipped'), ('delivered', 'Delivered')])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.id} for {self.user.username}"

