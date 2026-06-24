from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from cart.models import CartItem
from .models import Order, OrderItem
from django.shortcuts import redirect, get_object_or_404

@login_required
def place_order(request):
    cart_items = CartItem.objects.filter(user=request.user)
    if request.method == 'POST':
        if cart_items.exists():
            order = Order.objects.create(user=request.user)
            for item in cart_items:
                OrderItem.objects.create(
                    order=order,
                    medicine=item.medicine,
                    quantity=item.quantity
                )
            cart_items.delete()
            return redirect('order_history')
    return render(request, 'orders/place.html', {'cart_items': cart_items})

@login_required
def order_history(request):
    orders = Order.objects.filter(user=request.user).order_by('-timestamp')
    return render(request, 'orders/history.html', {'orders': orders})


@login_required
def cancel_order(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    if not hasattr(order, 'payment'):  # only allow cancel if unpaid
        order.status = 'Cancelled'
        order.save()
    return redirect('order_history')
