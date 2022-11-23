import stripe
from stripeTestTask import settings

stripe.api_key = settings.STRIPE_KEY


def create_session(order: dict) -> str:
    return stripe.checkout.Session.create(
        line_items=[{
            'price_data': {
                'currency': 'rub',
                'product_data': {
                    'name': f'Заказ № {order["id"]}',
                    'description': str(order["items"])
                },
                'unit_amount': order["price"],
            },
            'quantity': 1,
        }],
        mode='payment',
        success_url='http://localhost:4242/success',
        cancel_url='http://localhost:4242/cancel',
    )['id']
