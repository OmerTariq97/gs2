from django.shortcuts import render
import stripe
from django.conf import settings
from django.views import View
from django.views.generic import TemplateView
from django.http import JsonResponse
from .models import Products

stripe.api_key = settings.STRIPE_SECRET_KEY
# Create your views here.



def create_checkout_session(request):
    try:
        YOUR_DOMAIN="http://127.0.0.1:8000/"
        checkout_session = stripe.checkout.Session.create(
            line_items=[
                {
                    # Provide the exact Price ID (for example, pr_1234) of the product you want to sell
                    'price': 'price_1Mw82EAUSkTBXgbzyv58pVGI',
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url=YOUR_DOMAIN + '/success.html',
            cancel_url=YOUR_DOMAIN + '/cancel.html',
        )
    except Exception as e:
        return str(e)

    return redirect(checkout_session.url, code=303)

class ProductLandingPage(TemplateView):
    template_name="landing.html"