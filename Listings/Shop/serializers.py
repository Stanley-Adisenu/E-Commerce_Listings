from rest_framework import serializers
from .models  import Shop,Listings

class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = ['id','owner_id','shop_name','description','created_at','updated_at']

class ListingsSerializer(serializers.ModelSerializer):
    shop_id = ShopSerializer(read_only=True)
    class Meta:
        model = Listings
        fields = ['id', 'shop_id', 'title', 'description', 'price', 'quantity', 'created_at', 'updated_at']
 