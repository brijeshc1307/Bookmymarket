from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'govindfarming/index.html')
def transport(request):
    return render(request, 'govindfarming/transport.html')
def carservice(request):
    return render(request, 'govindfarming/carservice.html')
def tractorservice(request):
    return render(request, 'govindfarming/tractors.html')
def search(request):
    return render(request, 'govindfarming/index.html')
def invoice(request):
    return render(request, 'govindfarming/invoice.html')
def siup(request):
    return render(request, 'govindfarming/signup.html')
def lon(request):
    return render(request, 'govindfarming/login.html')
def empindex(request):
    return render(request, 'govindfarming/empindex.html')
def empuserwork(request):
    return render(request, 'govindfarming/empuserwork.html')
