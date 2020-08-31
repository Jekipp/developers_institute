from django.shortcuts import render
from .forms import OrderForm
from .models import Order

# Create your views here.


def index(request):
    form = OrderForm()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            new_order = form.save()
            if new_order.meat_tray:
                new_order.price += 20
            if new_order.fish_tray:
                new_order.price += 20
            new_order.save()
    return render(request, 'index.html', {'form': form})

def see_orders(request):
    orders = Order.objects.all()

    return render(request, 'order_list.html', {'orders': orders})