from django.contrib.auth import authenticate, login,logout # type: ignore
from django.contrib.auth.models import User# type: ignore
from django.http import HttpResponse# type: ignore
from django.shortcuts import render, redirect,get_object_or_404# type: ignore
from django.http import JsonResponse# type: ignore
import uuid
from items.models import items
from user_profile.models import user_profile_data
from .cart import Cart
from django.contrib import messages #type:ignore
from queries.models import Query

def login_page(request):
    if request.method == "POST":
        
        if request.POST.get('action') == 'login':
            username = request.POST.get('Username')
            password = request.POST.get('password')
         
            user = authenticate(request,username=username, password=password)

            if user is not None:
                login(request, user)
                request.session["username"] = user.username
                return redirect('home')
            else:
                data = {
                    'msg': "Invalid Credentials !!"
                }
                return render(request,'login.html',data)

        elif request.POST.get('action') == 'register':
            username = request.POST.get('Username')
            password = request.POST.get('password')
            email = request.POST.get('email')
            f_name = request.POST.get('f_name')
            l_name = request.POST.get('l_name')
            mob_number = request.POST.get('mob_number')
            branch = request.POST.get('branch')
            reg_number = request.POST.get('reg_number')
            user_img = request.FILES.get('user_img')

            if not User.objects.filter(username=username).exists():
                user = User.objects.create_user(username=username, password=password, email=email)
                user.save()
                data = {
                    'msg': "Successfully signed up!!"
                }
                user_profile = user_profile_data.objects.create(
                    user_name = username,
                    first_name=f_name,
                    last_name=l_name,
                    email = email,
                    phone_number=mob_number,
                    branch=branch,
                    reg_no=reg_number,
                    user_img=user_img
                )
                user_profile.save()

                return render(request,'login.html',data)
            else:
                data = {
                    'msg': "Username already exists. Please choose a different one."
                }
                return render(request,'login.html',data)

    return render(request, 'login.html')

def about(request):
    return render(request , 'about.html')

def home_page(request):
    
    return render(request, 'home_page.html')

def profile(request):
    details = user_profile_data.objects.get(user_name = request.session['username'])    
    return render(request, 'user_profile.html',{'details':details})

def cart_page(request):
    cart = Cart(request)
    products = cart.get_products()
    product_quantities = {str(product.id): cart.cart[str(product.id)]['quantity'] for product in products}
    total_price = cart.get_total()
    return render(request, 'cart_page.html', {
        'products': products,
        'total_price': total_price,
        'product_quantities': product_quantities
    })

def generate_upi_link(request):
    cart = Cart(request)
    merchant_upi_id = "loxai@axl"
    merchant_name = "Canteen Automation"
    transaction_id = str(uuid.uuid4())[:12]
    order_id = "order" + transaction_id[:8]
    amount = cart.get_total()
    currency = "INR"
    redirect_url = "/payment-success/"
    print(amount)

    upi_link = f"upi://pay?pa={merchant_upi_id}&pn={merchant_name}&tid={transaction_id}&tr={order_id}&tn=Canteen Order Payment&am={amount}&cu={currency}&url={redirect_url}"


    return JsonResponse({"upi_link": upi_link, "transaction_id": transaction_id})

def payment_success(request):
    print("Payment successful! Transaction ID:", request.GET.get("transaction_id"))

    return JsonResponse({"status": "success", "message": "Payment successful! Your order has been placed."})

def items_display(request, type):
    items_list = []
    if type=='all':
        items_list = items.objects.all()
    elif type[0]=='@':
        items_list = items.objects.filter(item_type=type[1:])
    else:
        if request.method == 'GET':
            search_item = request.GET.get('search', '')
            if search_item:
                items_list = items.objects.filter(item_name__icontains=search_item)
            else:
                items_list = items.objects.all()
    return render(request, 'items.html', {'items_list':items_list})

def logout_user(request):
    logout(request)
    return redirect('login')

def update(request):
    if request.method=="POST":
        new_fname = request.POST.get('firstName')
        new_lname = request.POST.get('lastName')
        new_mob = request.POST.get('phoneNumber')
        new_email = request.POST.get('email')
        new_branch = request.POST.get('branch')
        new_regno = request.POST.get('regno')
        user_data = user_profile_data.objects.get(user_name = request.session['username'])
        img_path = user_data.user_img
        user_data.delete()
        
        new_data = user_profile_data.objects.create(
            user_name = request.session['username'],
                    first_name=new_fname,
                    last_name=new_lname,
                    email = new_email,
                    phone_number=new_mob,
                    branch=new_branch,
                    reg_no=new_regno,
                    user_img=img_path
        )
        new_data.save()

    return redirect('profile')

def add_to_cart(request):
    cart = Cart(request)
    if request.POST.get("action") == "post":
        product_id = int(request.POST.get("product_id"))
        quantity = int(request.POST.get("quantity", 1))
        product = get_object_or_404(items, id=product_id)
        cart.add(product=product, quantity=quantity)
        messages.info(request, "PRODUCT ADDED TO CART")
        return JsonResponse({"Product": product.item_name})


def remove(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = request.POST.get('product_id')
        
        if product_id in cart.cart:
            del cart.cart[product_id]
            cart.save()
            messages.info(request, "PRODUCT REMOVED FROM CART")
            return JsonResponse({"Product": "Removed"})
        else:
            return JsonResponse({"error": "Product not found in cart"}, status=400)

    
def update_quantity(request):
    cart = Cart(request)
    if request.POST.get("action") == "post":
        product_id = int(request.POST.get("product_id"))
        quantity = int(request.POST.get("quantity"))
        cart.update_quantity(product_id=str(product_id), quantity=quantity)
        return JsonResponse({"success": True, "quantity": quantity})

def contact_page(request):
    return render(request , 'contact.html')

def submit(request):
    msg = ''
    if request.method =="POST":
        msg = 'Successfully submitted!!'
        topic = request.POST.get('topic')
        description = request.POST.get('description')
        new_query = Query.objects.create(
            username = request.session['username'],
            topic = topic,
            description = description
        )
        new_query.save()
    return render(request,'contact.html',{'msg':msg})