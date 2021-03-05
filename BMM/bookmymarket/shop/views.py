from django.contrib.auth.hashers import make_password, check_password
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Product
from .customer import Customer
from .order import Order
from math import ceil

# Create your views here.

def index(request):
    if request.method == 'POST':
        product = request.POST.get('product')
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(product)
            if quantity:
                cart[product] = quantity + 1
            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1
        request.session['cart'] = cart
        return redirect('ShopHome')

    else:
        cart = request.session.get('cart')
        if not cart:
            request.session.cart = {}

        products = Product.objects.all()
        allProds = []
        catprods = Product.objects.values('category', 'id')
        cats = {item["category"] for item in catprods}
        for cat in cats:
            prod = Product.objects.filter(category=cat)
            n = len(prod)
            nSlides = n // 4 + ceil((n / 4) - (n // 4))
            allProds.append([prod, range(1, nSlides), nSlides])
        params = {'allProds': allProds}
        return render(request, 'shop/index.html', params)


def fertilizers(request):
    products = Product.objects.all()
    allProds = []
    catprods = Product.objects.values('category', 'id')
    cats = {item["category"] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])
    params = {'allProds': allProds}
    return render(request, 'shop/fertilizers.html', params)
def agriMachinery(request):
    products = Product.objects.all()
    allProds = []
    catprods = Product.objects.values('category', 'id')
    cats = {item["category"] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])
    params = {'allProds': allProds}
    return render(request, 'shop/agriMachinery.html', params)
def pesticides(request):
    if request.method == 'POST':
        product = request.POST.get('product')
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(product)
            if quantity:
                cart[product] = quantity + 1
            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1
        request.session['cart'] = cart
        return redirect('Pesticides')
    else:
        cart = request.session.get('cart')
        if not cart:
            request.session.cart = {}

        products = Product.objects.all()
        allProds = []
        catprods = Product.objects.values('category', 'id')
        cats = {item["category"] for item in catprods}
        for cat in cats:
            prod = Product.objects.filter(category=cat)
            n = len(prod)
            nSlides = n // 3 + ceil((n / 3) - (n // 3))
            allProds.append([prod, range(1, nSlides), nSlides])
        params = {'allProds': allProds}
        return render(request, 'shop/pesticide.html', params)

def seed(request):
    products = Product.objects.all()
    allProds = []
    catprods = Product.objects.values('category', 'id')
    cats = {item["category"] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])
    params = {'allProds': allProds}
    return render(request, 'shop/seed.html', params)
def gardenning(request):
    products = Product.objects.all()
    allProds = []
    catprods = Product.objects.values('category', 'id')
    cats = {item["category"] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])
    params = {'allProds': allProds}
    return render(request, 'shop/gardenning.html', params)
def checkout(request):
    if request.method == 'POST':
        remove = request.POST.get('remove')
        product = request.POST.get('product')
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity==1:
                        cart.pop(product)
                    else:
                        cart[product] = quantity - 1
                else:
                    cart[product] = quantity + 1
            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1
        request.session['cart'] = cart
        return redirect('Checkout')
    else:
        ids = list(request.session.get('cart').keys())
        products = Product.get_product_by_id(ids)
        return render(request, 'shop/checkout.html', {'products': products})


def search(request):
    return render(request, 'shop/index.html')
def aboutus(request):
    return render(request, 'shop/aboutus.html')
def contactus(request):
    return render(request, 'shop/index.html')
def services(request):
    return render(request, 'shop/index.html')
def carrier(request):
    return render(request, 'shop/carrier.html')
def addcart(request):
    return render(request, 'shop/index.html')
def buynow(request):
    return render(request, 'shop/index.html')

def signup(request):
    if request.method == 'GET':
        return render(request, 'shop/signup.html')
    else:
        postData = request.POST
        customer_name = postData.get('Customername')
        customer_lname = postData.get('Customerlname')
        customer_gender = postData.get('Customergender')
        customer_designation = postData.get('Customerdesignation')
        phone = postData.get('Phone')
        email = postData.get('Email')
        dob_date = postData.get('Dobdate')
        password = postData.get('Password')
        repassword = postData.get('Repassword')
        value = {
            'customer_name': customer_name,
            'customer_lname': customer_lname,
            'customer_designation': customer_designation,
            'phone': phone,
            'email': email
        }


        error_message = None

        customer = Customer(customer_name=customer_name,
                            customer_lname=customer_lname,
                            customer_gender=customer_gender,
                            customer_designation=customer_designation,
                            phone=phone,
                            email=email,
                            dob_date=dob_date,
                            password=password)


        if len(customer_name) < 4:
            error_message = 'Enter your full name'

        elif len(customer_lname) < 2:
            error_message = 'Enter your full name'

        elif len(phone) != 10:
            error_message = 'Invalid phone number'

        elif password != repassword:
            error_message = 'Enter same password both..'

        elif customer.isExists():
            error_message = 'Your phone number is already registered..'

        if not error_message:
            customer.password = make_password(customer.password)
            customer.register()
            return redirect('ShopHome')
        else:
            data = {
                'error': error_message,
                'values': value
            }
            return render(request, 'shop/signup.html', data)

def login(request):
    if request.method == 'GET':
        return render(request, 'shop/login.html')
    else:
        postData = request.POST
        phone = postData.get('Phone')
        password = postData.get('Password')
        customer = Customer.get_cust_by_phone(phone)
        error_message = None
        if customer:
            flag = check_password(password , customer.password)
            if flag:
                request.session['customer_id'] = customer.id
                request.session['phone'] = customer.phone
                return redirect('ShopHome')
            else:
                error_message = 'Phone or Password invalid !'
        else:
            error_message = 'Phone or Password invalid !'
        return render(request, 'shop/login.html', {'error' : error_message})

def cheout(request):
    if request.method == 'GET':
        return render(request, 'shop/cheout.html')
    else:
        customer_fname = request.POST.get('customer_fname')
        customer_lname = request.POST.get('customer_lname')
        billing_country = request.POST.get('billing_country')
        date = request.POST.get('date')
        street = request.POST.get('street')
        apartment = request.POST.get('apartment')
        city = request.POST.get('city')
        state = request.POST.get('state')
        postcode = request.POST.get('postcode')
        phone = request.POST.get('phone')
        notes = request.POST.get('notes')
        customer = request.session.get('customer')
        cart = request.session.get('cart')
        products = Product.get_product_by_id(list(cart.keys()))

        for product in products:
            order = Order(customer = Customer(id = customer),
                          customer_fname = customer_fname,
                          customer_lname = customer_lname,
                          billing_country = billing_country,
                          street = street,
                          apartment = apartment,
                          city = city,
                          state = state,
                          postcode = postcode,
                          phone = phone,
                          notes = notes,
                          product = product,
                          price = product.price,
                          quantity = cart.get(str(product.id))
                        )
            order.save()
            request.session['cart'] = {}
            return redirect('Cheout')

def continueshopping(request):
    return render(request, 'shop/index.html')
def privacypolicy(request):
    return render(request, 'shop/privacypoliccy.html')
def returnpolicy(request):
    return render(request, 'shop/returnpolicy.html')
def productdetail(request):

    return render(request, 'shop/productdetail.html')
def customerdassboard(request):
    return render(request, 'shop/customerdassboard.html')
def logout(request):
    request.session.clear()
    return redirect('Login')


def invoice(request):
    return render(request, 'shop/invoice.html')
