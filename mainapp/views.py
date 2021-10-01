from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Mainapp
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def index(request):
    dances=Mainapp.objects.all()
    return render(request,'index.html',{'dances':dances})
def login(request):
    return render(request,'login.html')
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Вы успешно зарегестрировались!')
            return redirect('login')
        else:
            messages.error(request, 'Ошибка регистрации')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

