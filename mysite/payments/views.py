from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from orders.models import Order
from .models import Payment
import razorpay

client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))

def pay_order(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)

    # Create Razorpay Order
    amount_paise = int(order.total_price * 100)
    razorpay_order = client.order.create({
        "amount": amount_paise,
        "currency": "INR",
        "payment_capture": 1
    })

    # Save Payment object
    payment = Payment.objects.create(
        order=order,
        razorpay_order_id=razorpay_order['id']
    )

    context = {
        'order': order,
        'razorpay_order_id': razorpay_order['id'],
        'razorpay_key_id': settings.RAZORPAY_KEY_ID,
        'razorpay_amount': amount_paise,
    }
    return render(request, 'payments/pay.html', context)

@csrf_exempt
def verify_payment(request):
    if request.method == 'POST':
        order_id = request.POST.get('order_id')
        razorpay_order_id = request.POST.get('razorpay_order_id')
        razorpay_payment_id = request.POST.get('razorpay_payment_id')
        razorpay_signature = request.POST.get('razorpay_signature')

        order = get_object_or_404(Order, id=order_id, user=request.user)
        payment = order.payment

        # Verify signature
        try:
            params_dict = {
                'razorpay_order_id': razorpay_order_id,
                'razorpay_payment_id': razorpay_payment_id,
                'razorpay_signature': razorpay_signature
            }
            client.utility.verify_payment_signature(params_dict)

            # Update payment record
            payment.razorpay_payment_id = razorpay_payment_id
            payment.razorpay_signature = razorpay_signature
            payment.paid = True
            payment.save()

            return redirect('order_history')
        except razorpay.errors.SignatureVerificationError:
            return render(request, 'payments/failed.html')
