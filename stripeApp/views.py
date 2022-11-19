from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Item
from stripeApp import stripe_client
from rest_framework.renderers import TemplateHTMLRenderer
from django.shortcuts import render

@api_view()
def get_session_id(request, item_id):
    item = Item.objects.get(id=item_id)
    session_id = stripe_client.create_session(item)

    return Response(session_id)



