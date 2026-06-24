from django.shortcuts import render, get_object_or_404
from .models import Medicine

def medicine_list(request):
    medicines = Medicine.objects.all()
    return render(request, 'medicines/list.html', {'medicines': medicines})

def medicine_detail(request, id):
    medicine = get_object_or_404(Medicine, id=id)
    return render(request, 'medicines/detail.html', {'medicine': medicine})
