from django.contrib import admin
from django.urls import path

from stripeApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('buy/<int:order_id>/', views.create_session),
    path('order/<int:order_id>/', views.show_order_page),
    path('coupon/', views.create_coupon)
]
