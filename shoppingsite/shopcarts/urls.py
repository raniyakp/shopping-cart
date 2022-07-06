from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('signup/',views.signup,name='signup'),
    path('signin/',views.signin,name='signin'),
    path('signout/',views.signout,name='signout'),
    path('category/',views.category,name='category'),
    path('category/<int:category_id>/',views.subcategory,name='subcategory'),
    path('category/<int:category_id>/products/',views.products,name='products'),
    path('category/<int:category_id>/products/<int:product_id>',views.productdetails,name='productdetails'),
    path('cart/',views.cart,name='cart'),
    path('deleteitem/<int:cartitem_id>/',views.deleteitem, name='deleteitem'),
    path('order/',views.order, name='order'),
    path('cancelorder/<int:order_id>/',views.cancelorder, name='cancelorder'),
    path('profile/',views.profile, name='profile'),
]