from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Product
from django.urls import reverse_lazy
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

class ProductUpdateView(UpdateView):
  model = Product
  fields = ["name","price","description","validate",]
  template_name = "product_update_form.html"

class ProductDeleteView(DeleteView):
  model = Product
  success_url = reverse_lazy("core:list")
  template_name = "product_delete.html"