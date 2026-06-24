from django.contrib import admin
from .models import Medicine

@admin.register(Medicine)
class MedicineAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock', 'prescription_required')
    search_fields = ('name',)
    list_filter = ('prescription_required',)
