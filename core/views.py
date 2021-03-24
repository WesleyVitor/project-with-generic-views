from django.views.generic import ListView, DetailView, CreateView
from .models import Product

class ProductListView(ListView):
  model = Product
  template_name = "product_list.html"

class ProductDetailView(DetailView):
  model = Product
  template_name = "product_detail.html"

class ProductCreateView(CreateView):
  model = Product
  fields = ["name","price","description","validate",]
  template_name = "product_form.html"
  
