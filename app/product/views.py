from django.shortcuts import render
from rest_framework import viewsets,generics
from .models import Product
from .serializers import ProductSerializer
from rest_framework import filters
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status, viewsets
from users.models import User
from users.serializers import GetUserSerializer
import pusher
from size.serializers import SizeSerializer
from decouple import config
class ProductView(viewsets.ModelViewSet):
    permission_classes = (permissions.AllowAny, )
    filter_backends = [filters.SearchFilter]
    search_fields = ['location']
    queryset=Product.objects.all()
    serializer_class=ProductSerializer

    # def create(self,request):
    #     res = request.data
    #     item = ProductSerializer(data=res)
    #     item.is_valid(raise_exception=True)
    #     item.save()
    #     print(item.data)
    #     counter = 0
    #     for x in res.get('size'):
    #         size_data = {"size":x,"price":res.get('price')[counter],"product_id":item.data['id']}
    #         s_item = SizeSerializer(data=size_data)
    #         s_item.is_valid(raise_exception=True)
    #         s_item.save()
    #         counter = counter + 1
        
    #     return Response()




class SizeOfProduct(generics.GenericAPIView):
    def post(self,request,format=None):
        res = request.data

