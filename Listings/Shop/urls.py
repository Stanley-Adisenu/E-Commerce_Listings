from django.urls import path,include
from . import views

urlpatterns = [
    path('createshop/',views.create_shop),
    path('shopupdate/<int:pk>/',views.shop_update),
    path('listings/',views.listings_list),
    path('shoplist/<int:pk>/',views.shop_list),
    path('listdetail/<int:pk>/',views.list_detail),

]
