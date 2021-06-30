from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password

from store.models.items import Product
from store.models.customer import Customer

from django.views import View

from store.models.items import Product
from store.models.orders import Order


class OrderView(View):
    def get(self, request):
        customer = request.session.get('customer')
        orders = Order.get_order_by_customer(customer)
        print(orders)
        orders = orders.reverse()
        return render(request, 'orders.html' , {orders : orders})
