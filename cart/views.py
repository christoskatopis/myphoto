from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse
from photos.models import Photo
from .cart import Cart
from .forms import CartAddProductForm
from .models import Order
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import check_password
from django.core.mail import send_mail

@require_POST
def cart_add(request, id, slug=None):
    cart = Cart(request)
    product = get_object_or_404(Photo, id=id)
    product_id=product.id
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])
    return redirect('cart:cart_detail')


def cart_remove(request, id,slug=None):
    cart = Cart(request)
    product = get_object_or_404(Photo, id=id)
    cart.remove(product)
    return redirect('cart:cart_detail')

def cart_detail(request):
 cart = Cart(request)
 return render(request,'cart_detail.html',{"cart":cart})

@login_required(redirect_field_name=None)
def checkout(request):
 cart=Cart(request)
 user=request.user
 amount=cart.get_total_price()
 if amount > 0:
     form=AuthenticationForm()
     context1={"form":form}
     if request.POST:
         if request.POST.get('checkuser')==request.user.username:
             if check_password(request.POST.get('checkpass'),request.user.password):
                 neworder=Order(user=request.user,amount=amount)
                 neworder.save()
                 cart.clear()
                 context2={"order_message":"Your order has been submitted!Thank you for using myphoto."}
                 send_mail('my photo order','Your order: %d euros. Thank you for using myphoto \n -the myphoto team'%amount,'myphoto.team@gmail.com',[user.email])
                 return render(request,"order.html",context2)
             else:
                 context2={"order_message":"Your credentials are invalid!Please try again."}
                 return render(request,"order.html",context2)
                 
         else:
             context2={"order_message":"Your credentials are invalid!Please try again."}
             return render(request,"order.html",context2)
     else:
         return render(request,'checkout.html',context1)
 else:
     context2={"order_message":"Your cart is empty! Please add something before checking out."}
     return render(request,"order.html",context2)


