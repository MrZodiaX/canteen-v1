from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.urls import reverse

from .models import Menu, order 
# Create your views here.
def index(request):
    context = {
        "menu": Menu.objects.all()
        #"menu": topping.objects.all()
    }
    return render(request, "menu/index.html",context)

def Order(request, order_id):
    try:
        Order = order.objects.get(pk=order_id)  #primary key
    except order.DoesNotExist:
        raise Http404("Order does not exist")
    context ={
        "lmao" : Order
    }
    return render(request, "menu/menu.html",context)
