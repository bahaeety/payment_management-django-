from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.forms import AuthenticationForm 
from django.contrib.auth import login , authenticate
from .models import User
from django.views import View
from .form import UserForm
# Create your views here.
class user_signup(View):
    def post(self,request):
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            form = UserForm()
            return render(request, 'registration/signup.html', {'form':form})
    def get(self,request):
        form = UserForm()
        return render(request, 'registration/signup.html', {'form':form})
class user_login(View):
    def get(self,request):
        form = AuthenticationForm()
        return render(request, 'registration/login.html', {'form':form})
    def post(self,request):
        form = AuthenticationForm(request,data = request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user :
                login(request,user)
                return redirect('home')
        return render(request, 'registration/login.html')