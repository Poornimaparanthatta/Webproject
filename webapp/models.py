from django.db import models

# Create your models here.

class catdb(models.Model):
    Cat_Name=models.CharField(max_length=100,null=True,blank=True)
    Image=models.ImageField(upload_to="Category")
    Description=models.CharField(max_length=200,null=True,blank=True)

class prodb(models.Model):
    Category_Name=models.CharField(max_length=100,null=True,blank=True)
    Product_Name=models.CharField(max_length=100,null=True,blank=True)
    Product_Quantity=models.IntegerField(null=True,blank=True)
    Product_Price=models.IntegerField(null=True,blank=True)
    Product_descrption=models.CharField(max_length=100, null=True, blank=True)
    Product_Image=models.ImageField(upload_to="Product")

class contactdb(models.Model):
    Name=models.CharField(max_length=100, null=True, blank=True)
    Email=models.CharField(max_length=100, null=True, blank=True)
    Phone=models.IntegerField(null=True, blank=True)
    Message=models.CharField(max_length=100, null=True, blank=True)

class userdb(models.Model):
    usermail = models.CharField(max_length=100, null=True, blank=True)
    user = models.CharField(max_length=100, null=True, blank=True)
    passw = models.CharField(max_length=100, null=True, blank=True)
    con_passw = models.CharField(max_length=100, null=True, blank=True)

class cartdb(models.Model):
    proname = models.CharField(max_length=100, null=True, blank=True)
    User = models.CharField(max_length=100, null=True, blank=True)
    proquantity=models.IntegerField(null=True, blank=True)
    proprice=models.IntegerField(null=True, blank=True)


