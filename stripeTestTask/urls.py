from django.contrib import admin
from django.urls import path

from stripeApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('buy/<int:item_id>/', views.create_session),
    path('item/<int:item_id>/', views.show_item_page)
]
