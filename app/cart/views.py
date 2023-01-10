from django.shortcuts import render
from rest_framework import viewsets,generics
from .models import Cart
from .serializers import CartSerializer
from rest_framework import filters
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status, viewsets
from users.models import User
from product.views import Product
from product.serializers import ProductSerializer
from users.serializers import GetUserSerializer
import pusher
from decouple import config
class CartView(viewsets.ModelViewSet):
    filter_backends = [filters.SearchFilter]
    search_fields = ['location']
    queryset=Cart.objects.all()
    permissions_class = [permissions.AllowAny]
    serializer_class=CartSerializer

    def list(self,request):
        item = Cart.objects.filter(user_id=self.request.user.id)
        item = CartSerializer(item,many=True)
        for x in item.data:
            p_item = Product.objects.filter(id=x['product_id'])
            p_item = ProductSerializer(p_item,many=True)
            if(len(p_item.data)!=0):
                x['product_name'] = p_item.data[0]['product_name']
                x['image'] = p_item.data[0]['image']
        return Response(data=item.data)


