from stripeApp.models import Order


def get_order_data(order_id: int) -> dict:
    order = Order.objects.get(id=order_id)
    order_sum = 0
    items = []

    for item in order.items.all():
        order_sum += item.price
        items.append({'name': item.name,
                      'price': item.price,
                      'output_price': f'{item.price // 100}.{item.price % 100} руб.'
                      })
    if order.discount_coupon is not None:
        coupon_id = order.discount_coupon.coupon_id
    else:
        coupon_id = None

    return {'id': order_id, 'items': items, 'price': order_sum, 'coupon_id': coupon_id}

