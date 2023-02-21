from django.shortcuts import render
from rest_framework import viewsets,generics
from .models import Quote
from .serializers import QuoteSerializer
from rest_framework import filters
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status, viewsets
from users.models import User
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from django.template.loader import render_to_string, get_template
from django.core.mail import EmailMultiAlternatives
from users.serializers import GetUserSerializer
import pusher
from decouple import config
class QuoteView(viewsets.ModelViewSet):
    filter_backends = [filters.SearchFilter]
    search_fields = ['location']
    queryset=Quote.objects.all()
    permission_classes = (permissions.AllowAny, )
    serializer_class=QuoteSerializer
    
    def create(self,request):
        res = request.data
        ser = QuoteSerializer(data=res)
        ser.is_valid(raise_exception=True)
        ser.save()
        message = get_template('quote.html').render({"fullname":res.get('fullname'),"message":res.get('message'),"contact_number":res.get('contact_number'),"product_name":res.get('product_name')})
        msg = EmailMultiAlternatives('Quote', message,'rrglassandaluminum00@gmail.com', ['rrglassandaluminum00@gmail.com','fanepob312@octovie.com','meder11783@webonoid.com'])
        html_content = f'<p></p>'
        msg.content_subtype = "html"
        msg.send()
        print(ser.data)
        return Response(data=ser.data)



class Inquiry(generics.GenericAPIView):
    permission_classes = (permissions.AllowAny, )
    def post(self,request):
        res = request.data
        message = get_template('inquiry.html').render({"fullname":res.get('fullname'),"message":res.get('message'),"email":res.get('email')})
        msg = EmailMultiAlternatives(res.get('subject'), message,'rrglassandaluminum00@gmail.com', ['rrglassandaluminum00@gmail.com','fanepob312@octovie.com','meder11783@webonoid.com'])
        html_content = f'<p></p>'
        msg.content_subtype = "html"
        msg.send()
        return Response(status=status.HTTP_200_OK,data=[])

        