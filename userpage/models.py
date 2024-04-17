from django.db import models
# import datetime
from django.utils import timezone


# Create your models here.


class Category(models.Model):
    slug=models.CharField(max_length=150,null=False,blank=False)
    name=models.CharField(max_length=200,null=False,blank=False)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class Product(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    slug=models.CharField(max_length=500,null=False,blank=False)
    name=models.CharField(max_length=500,null=False,blank=False)
    product_image=models.FileField(upload_to='postmedia/',null=True)
    description=models.TextField(max_length=5000,null=False,blank=False)
    price=models.FloatField(null=False,blank=False)
    status=models.BooleanField(default=False,help_text="0=default, 1=Hidden")
    created_at=timezone.now()

    objects = models.Manager()
    def __str__(self):
        return self.name
    

# class Post(models.Model):
#     Title = models.CharField(max_length=255)
#     place=models.CharField(max_length=100)
#     post= models.FileField(upload_to='postmedia/')
#     upload_date = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.title