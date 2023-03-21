from django.urls import path
from app.views import *

urlpatterns = [
    path ('' ,index,name='index'),
    path ('shop', shop ,name='shop'),
    path('Shop_Details/',Shop_Details,name='Shop_Details'),
    path('shoping_cart/',shoping_cart,name='shoping_cart'),
    path('checkout/',checkout,name='checkout'),
    path('blog_details/',blog_details,name='blog_details'),
    path('blog/',blog,name='blog'),
    path('contact/',contact,name='contact'),
    
     
 
]  