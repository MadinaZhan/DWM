from django.shortcuts import render
from django.http import HttpResponse
from .models import Mainapp
from django.shortcuts import render

def index(request):
    dances=Mainapp.objects.all()
    return render(request,'index.html',{'dances':dances,'title':'dance with madina'})
