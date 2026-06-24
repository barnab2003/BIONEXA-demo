from django.shortcuts import render
from medicines.models import Medicine  # If medicine model exists

def home_view(request):
    featured = Medicine.objects.all()[:6]  # Get 6 top medicines
    return render(request, 'home/home.html', {'featured': featured})
