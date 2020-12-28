from django.urls import path

from . import views

urlpatterns = [
    path("",views.index, name="index"),
    path("<int:order_id>", views.Order, name="orderpage")
]