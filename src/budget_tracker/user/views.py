from django.shortcuts import render
from .models import User
from .form import UserForm
# Create your views here.
class user_view():
    def post(request):
        if request.method == 'POST':
            form = UserForm(request.POST)
            if form.is_valid():
                form.save()
        else:
            form = UserForm()
        return render(request, 'registration/signup.html', {'form':form})