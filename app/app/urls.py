from django.contrib import admin
from django.conf import settings
from django.urls import path
from django.urls.conf import include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from users.views import Login,GetUserView,Signup,ResetPassword,QuoteRequest,FindEmail
from size.views import SizeByProduct
from transaction.views import BulkTransact,Notify
from quote.views import Inquiry
from rest_framework import permissions
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
path('api/v1/admin/', admin.site.urls),
    path('api/v1/signup/', Signup.as_view(), name='Sign up'),
    path('api/v1/auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/quote/inquiry/', Inquiry.as_view(), name='token_refresh'),
    path('api/v1/auth/user/', GetUserView.as_view(), 
    name='auth_data'),
    path('api/v1/findemail/', FindEmail.as_view(), 
    name='auth_data'),
     path('api/v1/notif/', Notify.as_view(), 
    name='auth_data'),
    
    path('api/v1/login/', Login.as_view(), name='token_refresh'),
    # path('api/v1/quote/', QuoteRequest.as_view(), name='token_refresh'),
    path('api/v1/reset-password/', ResetPassword.as_view(), name='token_refresh'),
    path('api/v1/transaction/bulk/', BulkTransact.as_view(), name='token_refresh'),
    path('api/v1/size-by-product_id/', SizeByProduct.as_view(), name='token_refresh'),
    path('api/v1/users/', include('users.urls')),
    path('api/v1/product/', include('product.urls')),
    path('api/v1/size/', include('size.urls')),
    path('api/v1/quote/', include('quote.urls')),
    path('api/v1/quote/', include('quote.urls')),
    path('api/v1/cart/', include('cart.urls')),
    path('api/v1/transaction/', include('transaction.urls')),
    # path('api/v1/users/details/', GetUserView.as_view(), name='get_user'),
]