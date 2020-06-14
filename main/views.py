from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Diary, User
from .forms import RegisterForm, DiaryForm
from django.contrib.auth import get_user_model
from django.db.models import Count
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='login')
def home(request):
    obj = Diary.objects.filter(user_id=request.user.id)
    page = request.GET.get('page', 1)

    paginator = Paginator(obj, 10)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)

    context = {
        'obj': obj,
        'users':users,
        'page':page
    }
    return render(request, 'home.html', context)

def del_confirmation(request):
    obj = Diary.objects.all()
    context = {
        'obj':obj,
        'header':'Delete'
    }
    return render(request, 'del_confirmation.html', context)

def logout_confirmation(request):
    return render(request, 'logout_confirmation.html', {})

def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, user + ' successfully created')
            return redirect('login')
    else:
        form = RegisterForm()
    context = {
        'form': form,
        'header': 'Register'
    }
    return render(request, 'register.html', context)

def login_page(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password1')
         
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username Atau Password Salah')        
    context = {}
    return render(request, 'login.html', context)

def user_logout(request):
    logout(request)
    messages.success(request, 'Logout Success')
    return redirect('login')

@login_required(login_url='login')   
def create_diary(request):
    form = DiaryForm()
    user = User.objects.get(id=request.user.id)
    obj = Diary.objects.filter(user_id=request.user.id)
    
    if request.method == "POST":
        form = DiaryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            messages.error(request, 'Failed')
    context = {
        'form':form,
        'obj':obj,
        'user':user,
    
    }
    return render(request, 'form.html',context)

@login_required(login_url='login')
def view_diary(request, slug):
    obj = get_object_or_404(Diary, slug=slug, user=request.user)
    
    if request.method == "POST":
        form = DiaryForm(request.POST or None, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = DiaryForm(instance=obj)
    context = {
        'form': form,
        'obj':obj,  
    }
    return render(request, 'form.html', context)

@login_required(login_url='login')
def delete(request, slug):
    if request.user.is_authenticated():
        user = request.user
        obj = get_object_or_404(Diary, slug=slug)    
        
        if obj.user == user:
            obj.delete()
    else:
        return HttpResponseForbidden()
    return render(request, 'del_confirmation')  
    
    
