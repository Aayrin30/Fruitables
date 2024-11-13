from typing import Any
from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=30,blank=True,null=True)
    email = models.EmailField(blank=True,null=True)
    message = models.TextField()

    def __str__(self) -> str:
        return f"{self.name}-----{self.email}------{self.message}"



class Register(models.Model):
    name = models.CharField(max_length=30,blank=True,null=True)
    email = models.EmailField(unique=True,blank=True,null=True)
    image = models.ImageField(upload_to='media',blank=True,null=True)
    password = models.CharField(max_length=10,blank=True,null=True)
    address = models.CharField(max_length=255,blank=True,null=True)
    phone = models.CharField(max_length=15,blank=True,null=True)
    otp=models.IntegerField(blank=True,null=True)
    
    


    def __str__(self) -> str:
        return f"{self.name}-----{self.email}------{self.password}"
    

class Categorie(models.Model):
   
    name = models.CharField(max_length=30,blank=True,null=True)

    def __str__(self) -> str:
        return f"{self.name}"  

class Product(models.Model):
    Categorie_id=models.ForeignKey(Categorie,on_delete=models.CASCADE,blank=True,null=True)
    name = models.CharField(max_length=30,blank=True,null=True)
    quantity = models.IntegerField(default=1,blank=True,null=True)
    rating1= models.IntegerField(blank=True,null=True)
    halfrating = models.IntegerField(blank=True,null=True)
    image=models.ImageField(upload_to="media",blank=True,null=True)
    star = models.IntegerField(default=0)
    
    des=models.TextField()
    price=models.IntegerField()

    def __str__(self) -> str:
        return self.name



class CartItem(models.Model):
    user_id=models.ForeignKey(Register,on_delete=models.CASCADE,blank=True,null=True)
    product_id = models.ForeignKey(Product,on_delete=models.CASCADE,blank=True,null=True)
    image=models.ImageField(upload_to="media",blank=True,null=True)
    name = models.CharField(max_length=30,blank=True,null=True)
    price=models.IntegerField(blank=True,null=True)
    quantity = models.IntegerField(default=1,blank=True,null=True)
    total_price=models.IntegerField(blank=True,null=True)
    
    def __str__(self) -> str:
        return f"{self.quantity} x {self.product_id.name}"


class checkout(models.Model):
    firstname = models.CharField(max_length=30,blank=True,null=True)
    lastname = models.CharField(max_length=30,blank=True,null=True)
    companyname = models.CharField(max_length=30,blank=True,null=True)
    address =models.CharField(max_length=30,blank=True,null=True)
    city = models.CharField(max_length=30,blank=True,null=True)
    country = models.CharField(max_length=30,blank=True,null=True)
    zip = models.IntegerField()
    mobile = models.IntegerField()
    email = models.EmailField(blank=True,null=True)


    def __str__(self) -> str:
        return f"{self.firstname}---{self.lastname}---{self.companyname}---{self.address}---{self.city}---{self.country}---{self.zip}---{self.mobile}---{self.email}"


class order(models.Model):
    user_id=models.ForeignKey(Register,on_delete=models.CASCADE,blank=True,null=True)
    product_id = models.ForeignKey(Product,on_delete=models.CASCADE,blank=True,null=True)
    image=models.ImageField(upload_to="media",blank=True,null=True)
    name = models.CharField(max_length=30,blank=True,null=True)
    price=models.IntegerField(blank=True,null=True)
    quantity = models.IntegerField(default=1,blank=True,null=True)
    total_price=models.IntegerField(blank=True,null=True)
    datetime = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return f"{self.name}----{self.datetime} "
    


class Wishlist(models.Model):
    user_id=models.ForeignKey(Register,on_delete=models.CASCADE,blank=True,null=True)
    product_id = models.ForeignKey(Product,on_delete=models.CASCADE,blank=True,null=True)
    image=models.ImageField(upload_to="media",blank=True,null=True)
    name = models.CharField(max_length=30,blank=True,null=True)
    price=models.IntegerField(blank=True,null=True)
    total_price=models.IntegerField(blank=True,null=True)
    
    def __str__(self) -> str:
        return f"{self.name}"
    

class Rating(models.Model):
    user_id = models.ForeignKey(Register,on_delete=models.CASCADE,blank=True,null=True)
    product_id = models.ForeignKey(Product,on_delete=models.CASCADE,blank=True,null=True)
    rating = models.IntegerField(choices=[(i,i) for i in range(1,6)])
    name = models.CharField(max_length=30,blank=True,null=True)
    email = models.EmailField(blank=True,null=True)
    review = models.TextField(blank=True,null=True)
    datetime = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
