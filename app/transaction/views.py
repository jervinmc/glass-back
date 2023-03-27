from django.shortcuts import render
from rest_framework import viewsets,generics
from .models import Transaction
from .serializers import TransactionSerializer
from rest_framework import filters
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status, viewsets
from users.models import User
from users.serializers import GetUserSerializer
import pusher
from cart.models import Cart
from product.views import Product
from product.serializers import ProductSerializer
from decouple import config
pusher_client = pusher.Pusher(
  app_id=config('pusher_id'),
  key=config('pusher_key'),
  secret=config('secret_key'),
  cluster='ap1',
  ssl=True
)
class TransactionView(viewsets.ModelViewSet):
    filter_backends = [filters.SearchFilter]
    search_fields = ['location']
    queryset=Transaction.objects.all()
    permissions_class = [permissions.AllowAny]
    serializer_class=TransactionSerializer

    def list(self,request):
        item = Transaction.objects.all()
        item = TransactionSerializer(item,many=True)
        for x in item.data:
            p_item = Product.objects.filter(id=x['product_id'])
            p_item = ProductSerializer(p_item,many=True)
            if(len(p_item.data)!=0):
                x['product_name'] = p_item.data[0]['product_name']
                x['image'] = p_item.data[0]['image']
            u_item = User.objects.filter(id=x['user_id'])
            u_item = GetUserSerializer(u_item,many=True)
            if(len(u_item.data)!=0):
                x['users'] = u_item.data[0]
        return Response(data=item.data)




class Notify(generics.GenericAPIView):
    permission_classes=[permissions.AllowAny]
    def post(self,request):
        res = request.data
        pusher_client.trigger('notif', 'my-test', {'message': res.get('user_id'),'title': res.get('title'),'status': res.get('status')})
        return Response()

class ProductGetByUser(generics.GenericAPIView):
    permission_classes = (permissions.AllowAny, )
    def post(self,request):
        res = request.data
        item = Transaction.objects.filter(user_id=self.request.user.id)
        item = TransactionSerializer(item,many=True)
        for x in item.data:
            p_item = Product.objects.filter(id=x['product_id'])
            p_item = ProductSerializer(p_item,many=True)
            if(len(p_item.data)!=0):
                x['product_name'] = p_item.data[0]['product_name']
            else:
                pass
            
        serializers = UserSerializer(data=request.data)
        serializers.is_valid(raise_exception=True)
        serializers.save()
        return Response(status=status.HTTP_200_OK,data=serializers.data)


class BulkTransact(generics.GenericAPIView):
    permission_classes = (permissions.AllowAny, )
    def post(self,request):
        res = request.data
        for x in res.get('cart'):
            t_item = TransactionSerializer(data=x)
            t_item.is_valid(raise_exception=True)
            t_item.save()
            Cart.objects.filter(id=x['id']).delete()
        # item = Transaction.objects.filter(user_id=self.request.user.id)
        # item = TransactionSerializer(item,many=True)
        # for x in item.data:
        #     p_item = Product.objects.filter(id=x['product_id'])
        #     p_item = ProductSerializer(p_item,many=True)
        #     if(len(p_item.data)!=0):
        #         x['product_name'] = p_item.data[0]['product_name']
        #     else:
        #         pass
            
        # serializers = UserSerializer(data=request.data)
        # serializers.is_valid(raise_exception=True)
        # serializers.save()
        return Response(status=status.HTTP_200_OK,data=[])
