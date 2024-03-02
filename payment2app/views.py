from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import stripe
stripe.api_key = 'sk_test_51NZ7nbSItMY3F4AO9O1gEorbJfelBFXDN3dXm5XGqpulm8FoKVaMhKLYpbqkeKPwmJkHTG5khGIifKJJOuUJM16i00yhDJQBiY'
YOUR_DOMAIN = 'http://127.0.0.1:8000/'
@csrf_exempt
def create_checkout_session(request):
    peram=200*100
    ashok=peram
    checkout_session = stripe.checkout.Session.create(
            line_items=[
                {
                    # Provide the exact Price ID (for example, pr_1234) of the product you want to sell
                    'price_data': {
                    'currency': 'inr',
                    'unit_amount': ashok,
                    'product_data': {
                        'name': 'Product Name',  # Replace with actual product name
                        # Optionally add more product data as needed
                    },
                },
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url=YOUR_DOMAIN + 'success',
            cancel_url=YOUR_DOMAIN + 'cancel',
        )
    return redirect(checkout_session.url, code=303)

def home(request):
    return render(request,'checkout.html')
def success(request):
    return HttpResponse('this is success')
def cancel(request):
    return HttpResponse('this is cancel')
