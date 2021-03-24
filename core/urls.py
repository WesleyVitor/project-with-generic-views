from django.urls import path

from . import views

app_name = "core"

urlpatterns = [
  path("",views.ProductListView.as_view(),name="list"),
]