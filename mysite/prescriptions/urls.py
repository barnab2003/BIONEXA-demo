from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.upload_prescription, name='upload_prescription'),
    path('', views.list_prescriptions, name='list_prescriptions'),
    path('admin-review/', views.admin_prescription_review, name='admin_prescription_review'),

]
