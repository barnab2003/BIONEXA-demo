from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Prescription

@login_required
def upload_prescription(request):
    if request.method == 'POST' and request.FILES.get('file'):
        Prescription.objects.create(user=request.user, file=request.FILES['file'])
        return redirect('list_prescriptions')
    return render(request, 'prescriptions/upload.html')

@login_required
def list_prescriptions(request):
    prescriptions = Prescription.objects.filter(user=request.user).order_by('-uploaded_at')
    return render(request, 'prescriptions/list.html', {'prescriptions': prescriptions})

from django.contrib.admin.views.decorators import staff_member_required

@staff_member_required
def admin_prescription_review(request):
    from .models import Prescription
    if request.method == 'POST':
        pid = request.POST.get('prescription_id')
        action = request.POST.get('action')
        presc = Prescription.objects.get(id=pid)
        if action == 'approve':
            presc.status = 'Approved'
        elif action == 'reject':
            presc.status = 'Rejected'
        presc.save()
    pending_prescriptions = Prescription.objects.filter(status='Pending')
    return render(request, 'prescriptions/admin.html', {'pending_prescriptions': pending_prescriptions})
