from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from stripeApp import stripe_client
from .models import Item


@api_view()
def create_session(request, item_id):
    item = Item.objects.get(id=item_id)
    session_id = stripe_client.create_session(item)

    return Response({'id': session_id})


@api_view()
def show_page(request, item_id):
    item = Item.objects.get(id=item_id)
    ctx = {
        'item_id': item_id,
        'name': item.name,
        'description': item.description,
        'price': f'{item.price // 100}.{item.price % 100} руб.',
    }
    return render(request, "test.html", context=ctx)
