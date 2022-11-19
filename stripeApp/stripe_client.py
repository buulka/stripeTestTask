import stripe
from .models import Item
from stripeTestTask import settings

stripe.api_key = settings.STRIPE_KEY


def create_session(item: Item) -> str:
    return stripe.checkout.Session.create(
        line_items=[{
            'price_data': {
                'currency': 'rub',
                'product_data': {
                    'name': item.name,
                    'description': item.description
                },
                'unit_amount': item.price,
            },
            'quantity': 1,
        }],
        mode='payment',
        success_url='http://localhost:4242/success',
        cancel_url='http://localhost:4242/cancel',
    )['id']
