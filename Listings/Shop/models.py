from django.db import models

# Create your models here.
class Shop(models.Model):
    owner_id = models.CharField(max_length=500)
    shop_name = models.CharField(max_length=500)
    description = models.TextField()
    created_at = models.TimeField(auto_now_add=True)
    updated_at = models.TimeField(auto_now=True)

    def __str__(self):
        return self.shop_name
    

class Listings(models.Model):
    shop_id = models.ForeignKey(Shop, on_delete=models.CASCADE)
    title = models.CharField(max_length=500)
    description = models.TextField()
    price = models.FloatField()
    quantity = models.IntegerField(default=1,blank=True)
    created_at = models.TimeField(auto_now_add=True,null=True,blank=True)
    updated_at = models.TimeField(auto_now=True,null=True,blank=True)

    def __str__(self):
        return self.title
    