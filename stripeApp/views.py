from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from stripeApp import stripe_client
from .models import Order


@api_view()
def create_session(request, order_id):
    order_data = get_order_data(order_id)

    session_id = stripe_client.create_session(order_data)

    return Response({'id': session_id})


@api_view()
def show_order_page(request, order_id):
    order_data = get_order_data(order_id)
    ctx = {
        'item_id': order_id,
        'name': f'Заказ № {order_id}',
        'description': order_data['items'],
        'price': f'{order_data["price"] // 100}.{order_data["price"] % 100} руб.',
    }
    return render(request, "test.html", context=ctx)


def get_order_data(order_id):
    order = Order.objects.get(id=order_id)
    order_sum = 0
    items = []

    for item in order.items.all():
        order_sum += item.price
        items.append({'name': item.name,
                      'price': item.price,
                      'output_price': f'{item.price // 100}.{item.price % 100} руб.'
                      })

    return {'id': order_id, 'items': items, 'price': order_sum}
