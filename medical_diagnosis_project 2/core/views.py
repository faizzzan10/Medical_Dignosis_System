
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm
from . import rules

def home(request):
    return render(request, 'home.html')

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('diagnosis_home')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('diagnosis_home')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('home')

@login_required
def diagnosis_home(request):
    return render(request, 'diagnosis_home.html')

@login_required
def run_forward(request):
    facts = []
    inferred = []
    if request.method == 'POST':
        facts = request.POST.getlist('facts')
        inferred = rules.forward_chain(facts)
    return render(request, 'diagnosis_result.html', {'facts': facts, 'inferred': inferred})

@login_required
def backward_wizard(request):
    result = None
    rule = None
    goal = None
    if request.method == 'POST':
        goal = request.POST.get('goal')
        facts = request.POST.getlist('facts')
        result, rule = rules.backward_chain_wizard(goal, facts)
    return render(request, 'backward_wizard.html', {'result': result, 'rule': rule, 'goal': goal})
