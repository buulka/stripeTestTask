from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from stripeApp import stripe_client, logic
from .models import Discount, Tax


@api_view()
def create_session(request: WSGIRequest, order_id: int) -> Response:
    order_data = logic.get_order_data(order_id)

    session_id = stripe_client.create_session_api(order_data)

    return Response({'id': session_id})


@api_view()
def show_order_page(request: WSGIRequest, order_id: int) -> HttpResponse:
    order_data = logic.get_order_data(order_id)

    if order_data["coupon_id"] is not None:
        percent = Discount.objects.get(coupon_id=order_data["coupon_id"]).amount
        if percent // 100 != 0:
            percent = str(percent % 100) + '.' + str(percent // 100)
    else:
        percent = None

    ctx = {
        'item_id': order_id,
        'name': f'Заказ № {order_id}',
        'description': order_data['items'],
        'price': f'{order_data["price"] // 100}.{order_data["price"] % 100} руб.',
        'discount': percent
    }
    return render(request, "order.html", context=ctx)


@api_view(["POST"])
def create_coupon(request: WSGIRequest) -> Response:
    amount = request.data["percent"]

    coupon_id = stripe_client.create_coupon_api(amount)
    new_discount = Discount.objects.create(amount=amount, coupon_id=coupon_id)
    new_discount.save()

    return Response(status=status.HTTP_201_CREATED)