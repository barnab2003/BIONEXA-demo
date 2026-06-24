from django.urls import path
from . import views

urlpatterns = [
    path('place/', views.place_order, name='place_order'),
    path('history/', views.order_history, name='order_history'),
    path('cancel/<int:order_id>/', views.cancel_order, name='cancel_order'),

]
