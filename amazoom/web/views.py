from django.shortcuts import render
from django.views.generic.list import ListView

from .models import Product


class ProductListView(ListView):
	template_name = 'product_list.html'
	model = Product

