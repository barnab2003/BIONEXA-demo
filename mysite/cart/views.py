from django.shortcuts import render, redirect, get_object_or_404
from .models import CartItem
from medicines.models import Medicine
from django.contrib.auth.decorators import login_required
from prescriptions.models import Prescription

@login_required
def add_to_cart(request, medicine_id):
    medicine = get_object_or_404(Medicine, id=medicine_id)

    if medicine.prescription_required:
        has_approved = Prescription.objects.filter(user=request.user, status='Approved').exists()
        if not has_approved:
            return render(request, 'cart/prescription_required.html', {'medicine': medicine})

    cart_item, created = CartItem.objects.get_or_create(user=request.user, medicine=medicine)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('view_cart')
@login_required
def view_cart(request):
    cart_items = CartItem.objects.filter(user=request.user)
    return render(request, 'cart/view.html', {'cart_items': cart_items})

@login_required
def remove_from_cart(request, item_id):
    item = get_object_or_404(CartItem, id=item_id, user=request.user)
    item.delete()
    return redirect('view_cart')
