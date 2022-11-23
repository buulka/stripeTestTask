from django.contrib import admin
from .models import Item, Order


admin.site.register([Item, Order])
