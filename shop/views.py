from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.edit import CreateView
from rest_framework import viewsets
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Product, Purchase
from .serializers import ProductSerializer
# Create your views here.
def index(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'shop/index.html', context)

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
        return redirect('index')
    else:
        form = UserCreationForm()
    form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

def login(request):
    return render(request, 'registration/login.html')

def my_purchase(request):
    username = None
    if request.user.is_authenticated:
        username = request.user.username
    model = Purchase.objects.filter(person = username)
    return render(request, 'shop/purchase.html', {'purchase': model})

class PurchaseCreate(CreateView):
    model = Purchase
    fields = ['product', 'person', 'address']

    def form_valid(self, form):
        self.object = form.save()
        return HttpResponse(f'Спасибо за покупку, {self.object.person}!')


class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


