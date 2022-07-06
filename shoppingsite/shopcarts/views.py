from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.db.models import Sum,F

from .forms import *

from shopcarts.models import *
from shopcarts.tasks import mailing

def index(request):
    if request.user.is_authenticated:
        return redirect('/category')
    return redirect('/home')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user=form.save()
            
            return redirect('/')
    else:
        form = SignupForm()
    return render(request, 'shopcarts/signup.html', {'form': form})

def signin(request):
    if request.user.is_authenticated:
        return redirect('/category')
        
    if request.method=='POST':
        username= request.POST['username']
        password= request.POST['password']

        user=auth.authenticate(username=username,password=password)
        
        if user is not None:
            auth.login(request,user)
            return redirect('/category')
        else:
            messages.error(request,'Invalid username or password!')
            return redirect('/signin')
    else:
        return render(request, 'shopcarts/signin.html')

def home(request):
    return render(request,'shopcarts/homepage.html')

@login_required
def signout(request):
    auth.logout(request)
    return redirect('/home')

@login_required
def category(request):
    category=Category.objects.filter(parent__isnull=True)
    context={'category':category}
    return render(request, 'shopcarts/category.html',context)

@login_required
def subcategory(request, category_id):
    category = Category.objects.filter(parent__id=category_id)
    if not category:
        return redirect('products/')
    return render(request, 'shopcarts/category.html', {'category': category})

@login_required
def products(request,category_id):
    category = Category.objects.get(pk=category_id)
    product =  Product.objects.filter(category__id=category_id)
    context = {'product':product,'category':category}
    return render(request, 'shopcarts/products.html', context)

@login_required
def cart(request):
    cartitem = CartItem.objects.filter(cart__user=request.user)
    context = {'cartitem':cartitem}
    if cartitem:
        return render(request, 'shopcarts/cart.html',context)
    else:
        return render(request,'shopcarts/emptycart.html')

@login_required
def productdetails(request,category_id,product_id):
    if request.method=='POST':
        quantity = request.POST['qty']
        product = Product.objects.get(pk=product_id)
        cart, created = Cart.objects.get_or_create(user=request.user)
        cart.user=request.user
        item = CartItem.objects.create(product=product,quantity=quantity,cart=cart)
        item.price = float(quantity) * float(product.rate)
        item.save()
        return redirect('/cart')
    product = Product.objects.get(pk=product_id)
    context = {'product':product}
    return render(request,'shopcarts/productdetails.html',context)

@login_required
def deleteitem(request,cartitem_id):
    cartitem = CartItem.objects.get(pk=cartitem_id)
    cartitem.delete()
    return redirect('/cart')

@login_required
def order(request):
    if not Order.objects.filter(user=request.user) and request.method != 'POST' :
        return render(request, 'shopcarts/noorder.html')

    userprofile=request.user.userprofile

    if not (userprofile.address and userprofile.state and userprofile.pincode):
        return render(request,'shopcarts/addaddress.html')

    cart = Cart.objects.get(user=request.user)
    cartitems = CartItem.objects.filter(cart=cart)
    products = Product.objects.filter(id = F('cartitem__product__id'))

    if request.method == 'POST' and cartitems:
        order = Order.objects.create(user=request.user,status='Ordered')
        for product in products:
            item = CartItem.objects.get(product__id=product.id)
            productorder = ProductOrder.objects.create(order=order, product=product, quantity=item.quantity, price=item.price)
            
        order.total_cost = cartitems.aggregate(Sum('price')).get('price__sum')
        order.shippingaddress = request.user.userprofile.address +','+ request.user.userprofile.state + ','+ str(request.user.userprofile.pincode)
        order.save()
        cartitems.delete()
        mailing.delay(request.user.email, request.user.first_name, order.id)
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    productlist = ProductOrder.objects.all()
    context = {'orders':orders, 'productlist':productlist, 'userprofile':request.user.userprofile}
    return render(request,'shopcarts/order.html',context)

@login_required
def cancelorder(request,order_id):
    Order.objects.filter(pk=order_id).update(status='Cancelled')
    return redirect('/order')

@login_required
def profile(request):
    if request.method == 'POST':
    
        user = request.user
        userprofile = UserProfile.objects.get(user=user)
        
        if request.POST['photo']:
            userprofile.photo = request.FILES['photo']
        if request.POST['phone']:
            userprofile.phone = request.POST['phone']
        if request.POST['address']:
            userprofile.address = request.POST['address']
        if request.POST['state']:
            userprofile.state = request.POST['state']
        if request.POST['pincode']:
            userprofile.pincode = request.POST['pincode']

        userprofile.save()

        return redirect('/')

    return render(request,'shopcarts/profile.html')



        
    