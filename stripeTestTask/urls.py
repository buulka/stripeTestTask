from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

from stripeApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('buy/<int:item_id>/', views.get_session_id),
]
