from django.shortcuts import render

# Create your views here.
def index(request):
    
    
    return render(request,'index.html')
def shop(requests):
    return render(requests ,'parts\shop.html')
def Shop_Details(request):
    return render(request ,'pages\Shop_Details.html')
def shoping_cart(request):
    return render(request ,'pages\shoping_cart.html')
def checkout(request):
    return render(request ,'pages\checkout.html')
def blog_details(request):
    return render(request ,'pages\log_details.html')
def blog(requests):
    return render(requests ,'parts\log.html') 
def contact(requests):
    return render(requests ,'parts\contact.html')
    
    