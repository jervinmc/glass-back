from django.shortcuts import render
from rest_framework import viewsets,generics
from .models import User
from .serializers import UserSerializer
from rest_framework import filters
from rest_framework import status, viewsets
import random
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from django.core.mail import EmailMultiAlternatives
from rest_framework import mixins, viewsets, permissions
from django.template.loader import render_to_string, get_template
import string
from users.serializers import GetUserSerializer,UserSerializer
import random
import string
from rest_framework.response import Response
class UserView(viewsets.ModelViewSet):  
    filter_backends = [filters.SearchFilter]
    search_fields = ['category','price','name','descriptions']
    queryset=User.objects.all()
    permission_classes = (permissions.AllowAny, )
    serializer_class=UserSerializer
    
    # def create(self,request):
    #     res = request.data
    #     serializers = UserSerializer(data=res)
    #     serializers.is_valid(raise_exception=True)
    #     serializers.save()
    #     message = get_template('otp.html').render({"email":request.data.get('email')})
    #     msg = EmailMultiAlternatives('OTP', message,'naidtngcolo@gmail.com', [request.data.get('email')])
    #     html_content = f'<p>This is an<strong>important</strong> message.</p>'
    #     msg.content_subtype = "html"
    #     msg.send()
    #     return Response()
        


class Login(generics.GenericAPIView):
    def post(self,request,format=None):
        try:
            res = request.data
            items = User.objects.filter(email=res.get('email'),password=res.get('password')).count()
            if(items>0):
               items = User.objects.filter(email=res.get('email'),password=res.get('password')) 
               items = UserSerializer(items,many=True)       
               return Response(status=status.HTTP_200_OK,data=items.data)
            else:
               return Response(status=status.HTTP_404_NOT_FOUND,data=items.data)
            
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_404_NOT_FOUND,data=[])



def id_generator(size=8, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))
class VerifyUser(generics.GenericAPIView):
    def get(self,request,format=None,email=None):
        User.objects.filter(email=email).update(is_verified=True)
        return Response()



class ResetPassword(generics.GenericAPIView):
    permission_classes = (permissions.AllowAny, )
    def post(self,request):
        res = request.data
        password = id_generator()
        print(password)
        print(res.get('email'))
        item = User.objects.filter(email=res.get('email')).first()
        serializer = UserSerializer(item,data={"password":password})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        message = get_template('mail.html').render({"password":password})
        msg = EmailMultiAlternatives('OTP', message,'bitbobms@gmail.com', [res.get('email')])
        html_content = f'<p></p>'
        msg.content_subtype = "html"
        msg.send()
        return Response()

class QuoteRequest(generics.GenericAPIView):
    permission_classes = (permissions.AllowAny, )
    def post(self,request):
        res = request.data
        message = get_template('mail.html').render({"fullname":res.get('fullname'),"message":res.get('message'),"contact_number":res.get('contact_number'),"product_name":res.get('product_name')})
        msg = EmailMultiAlternatives('OTP', message,'rrglassandaluminum00@gmail.com', ['rrglassandaluminum00@gmail.com','fanepob312@octovie.com'])
        html_content = f'<p></p>'
        msg.content_subtype = "html"
        msg.send()
        return Response()

class Signup(generics.GenericAPIView):
    permission_classes = (permissions.AllowAny, )
    def post(self,request):
        serializers = UserSerializer(data=request.data)
        serializers.is_valid(raise_exception=True)
        serializers.save()
        message = get_template('verification.html').render({"id":serializers.data.get('id')})
        print(serializers.data)
        msg = EmailMultiAlternatives('Verification', message,'rrglassandaluminum00@gmail.com', [serializers.data.get('email')])
        html_content = f'<p></p>'
        msg.content_subtype = "html"
        msg.send()
        return Response(status=status.HTTP_200_OK,data=serializers.data)



class GetUserView(generics.GenericAPIView):

    # # permission_classes = (IsAuthenticated, )

    # queryset = User.objects.none()
    serializer_class = GetUserSerializer
    def get(self, request, format=None):
        print("okay")
        user_serializer = GetUserSerializer(request.user)
        return Response({'user': user_serializer.data}, status=status.HTTP_200_OK)

def id_generator(size=8, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))



class FindEmail(generics.GenericAPIView):
    permission_classes = (permissions.AllowAny, )
    def post(self,request):
        res = request.data
        items = User.objects.filter(email=res.get('email'))
        items = GetUserSerializer(items,many=True)
        print(items.data)
        return Response(status=status.HTTP_200_OK,data=items.data)