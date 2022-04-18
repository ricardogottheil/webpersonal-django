from django.shortcuts import render
from .models import Project

# Create your views here.
def briefcase(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/briefcase.html', {'projects': projects})