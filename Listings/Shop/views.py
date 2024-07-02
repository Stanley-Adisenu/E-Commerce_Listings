from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from django.db.models import Q
from .models import Shop,Listings
from .serializers import ShopSerializer,ListingsSerializer

# Create your views here.
@api_view(['GET','POST'])
def create_shop(request):
    if request.method == 'POST':
        serializer = ShopSerializer(data=request.data)  
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'GET':
        shops = Shop.objects.all()
        serializer = ShopSerializer(shops, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
@api_view(['GET','PATCH'])
def shop_update(request,pk):
    if request.method == 'GET':
        shop = get_object_or_404(Shop,id=pk)
        serializer = ShopSerializer(shop)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    if request.method == 'PATCH':
        shop = get_object_or_404(Shop,id=pk)
        serializer = ShopSerializer(shop,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def listings_list(request):
    if request.method == 'GET':
        query = request.GET.get('q', '')
        if query:
            listing = Listings.objects.filter(
                Q(title__icontains=query) |
                Q(description__icontains=query)
            )
        else:
            listing = Listings.objects.all()
        
        serializer = ListingsSerializer(listing, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST','GET'])
def shop_list(request, pk):
    shop = get_object_or_404(Shop,id=pk)
    if request.method == 'POST':
        listing = Listings.objects.create(
            shop_id = shop,
            title =request.data.get('title'),
            description =request.data.get('description'),
            price =request.data.get('price'),
            quantity =request.data.get('quantity')
        )
        return Response(ListingsSerializer(listing).data,status=status.HTTP_201_CREATED)
    
    #For listing all the listings in a shop
    if request.method == 'GET':
        shop = get_object_or_404(Shop, id=pk)
        query = request.GET.get('q', '')
    
        if query:
            shop_listings = Listings.objects.filter(
                Q(shop_id=shop) &
                (Q(title__icontains=query) | Q(description__icontains=query))
            )
        else:
            shop_listings = Listings.objects.filter(shop_id=shop)
        
        serializer = ListingsSerializer(shop_listings, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET','PATCH','DELETE'])
def list_detail(request,pk):
    if request.method == 'GET':
        item = get_object_or_404(Listings,id=pk)
        serializer = ListingsSerializer(item)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    if request.method == 'PATCH':
        item = get_object_or_404(Listings,id=pk)
        serializer = ListingsSerializer(item,data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    if request.method=='DELETE':
        item = get_object_or_404(Listings,id=pk)
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    



    
    
