from django.shortcuts import render

from .models import Task, Aim

from django.utils import timezone

from .forms import TaskForm, AimForm
from django.contrib.auth import authenticate
from django.views.generic import DeleteView
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render
from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect

# Create your views here.



def index(request):

    return render(request, 'main/login.html')


def task(request, pk):

    aims = Aim.objects.filter(taskAim=pk)
    task = get_object_or_404(Task, pk=pk)
    if request.method == "POST":
        aimForm = AimForm(request.POST)
        if aimForm.is_valid():
            aim = aimForm.save(commit=False)
            Aim.author = request.user
            aim.save()
            return redirect('task', pk=task.pk)
    else:
        aimForm = AimForm()
    return render(request, 'main/task.html', {'task': task, 'aims': aims, 'aimForm': aimForm})



def taske(request):

    return render(request, 'main/task.html')


def home(request):
    tasks = Task.objects.all()
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            Task.author = request.user
            task.date = timezone.now()
            task.save()
            return redirect('home')
    else:
        form = TaskForm()
    return render(request, 'main/index.html', {'tasks': tasks, 'form': form})



def account(request):
    return render(request, 'main/account.html')




