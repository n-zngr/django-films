from django.contrib import messages
from django.shortcuts import redirect, render
from users.forms import RegisterForm
from django.contrib.auth.forms import UserCreationForm

def register(request):
    if request.method =='POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            messages.success(request, f'Willkommen {username}! Du bist nun eingeloggt.')
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()

    return render(request, 'users/register.html',{'form':form})