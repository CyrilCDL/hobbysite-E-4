from .models import Product, ProductType
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

class ProductListView(ListView):
    model = ProductType
    template_name = 'items_list.html'

class ProductDetailView(DetailView):
    model = Product
    template_name = 'items_detail.html'