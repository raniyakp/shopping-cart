from django.urls import path

from rest_framework.authtoken.views import obtain_auth_token

from shopcarts.api import views

urlpatterns = [
     path('cartapi/', views.CartItemView.as_view(), name='cart-api'),
     path('signinapi/',views.signin, name='signin-api'),
     path('signoutapi/',views.Signout.as_view(), name='signout-api'),
]