from django.shortcuts import render
from rest_framework import viewsets,generics
from .models import Size
from .serializers import SizeSerializer
from rest_framework import filters
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status, viewsets
from users.models import User
from users.serializers import GetUserSerializer
import pusher
from decouple import config
class SizeView(viewsets.ModelViewSet):
    filter_backends = [filters.SearchFilter]
    search_fields = ['location']
    queryset=Size.objects.all()
    permissions_class = [permissions.AllowAny]
    serializer_class=SizeSerializer

    def create(self,request):
        res = request.data
        counter = 0
        Size.objects.filter(product_id=res.get('product_id')).delete()
        for x in res.get('size'):
            size_data = {"size":x,"price":res.get('price')[counter],"color":res.get('color')[counter],"product_id":res.get('product_id')}
            s_item = SizeSerializer(data=size_data)
            s_item.is_valid(raise_exception=True)
            s_item.save()
            counter = counter + 1
        return Response()



class SizeByProduct(generics.GenericAPIView):
    permission_classes = (permissions.AllowAny, )
    def post(self,request):
        res = request.data
        item = Size.objects.filter(product_id=res.get('product_id'))
        item = SizeSerializer(item,many=True)
        return Response(status=status.HTTP_200_OK,data=item.data)