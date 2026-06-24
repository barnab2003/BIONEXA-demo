from django.urls import path
from . import views

urlpatterns = [
    path('', views.medicine_list, name='medicine_list'),
    path('<int:id>/', views.medicine_detail, name='medicine_detail'),
]
