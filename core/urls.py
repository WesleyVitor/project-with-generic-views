from django.urls import path

from . import views

app_name = "core"

urlpatterns = [
  path("",views.ProductListView.as_view(),name="list"),
  path("detail/<int:pk>",views.ProductDetailView.as_view(),name="detail"),
  path("new/",views.ProductCreateView.as_view(),name="create"),
  path("update/<int:pk>/",views.ProductUpdateView.as_view(),name="update"),
  path("delete/<int:pk>/",views.ProductDeleteView.as_view(),name="delete"),
]