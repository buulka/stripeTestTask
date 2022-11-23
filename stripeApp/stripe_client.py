import stripe
from stripeTestTask import settings

stripe.api_key = settings.STRIPE_KEY


def create_session_api(order: dict) -> str:
    line_items = [{
        'price_data': {
            'currency': 'rub',
            'product_data': {
                'name': f'Заказ № {order["id"]}',
                'description': str(order["items"])
            },
            'unit_amount': order["price"],
        },
        'quantity': 1,
    }]
    mode = 'payment'
    success_url = 'http://localhost:8000/admin'
    cancel_url = 'http://localhost:8000/'

    if order["coupon_id"] is not None:
        return stripe.checkout.Session.create(
            line_items=line_items,
            mode=mode,
            discounts=[{
                'coupon': order["coupon_id"],
            }],
            success_url=success_url,
            cancel_url=cancel_url,
        )["id"]

    return stripe.checkout.Session.create(
            line_items=line_items,
            mode=mode,
            success_url=success_url,
            cancel_url=cancel_url
    )["id"]


def create_coupon_api(percent: int) -> str:
    return stripe.Coupon.create(
        percent_off=str(percent % 100) + '.' + str(percent // 100),
        duration="forever"
    )['id']
