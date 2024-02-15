import stripe
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from basket.basket import Basket


@login_required
def BasketView(request):
    
    basket = Basket(request)
    total = str(basket.get_total_price())
    total = total.replace(".", "")
    total = int(total)
    
    stripe.api_key = settings.STRIPE_SECRET_KEY
    intent = stripe.PaymentIntent.create(
        amount=total,
        currency='gbp',
        metadata={'user_id': request.user.id}
    )
    
    return render(request, "payment/home.html", {"client_secret": intent.client_secret})