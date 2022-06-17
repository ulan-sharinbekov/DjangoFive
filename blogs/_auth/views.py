from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .form import SignUpForm
# Create your views here.

def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            try:
                user = User.objects.create_user(**form.cleaned_data)
                user.save()
                return redirect('add_user')
            except:
                form.add_error(None, "Ошибка создания")

    else:
        form = SignUpForm()
    return render(request, "signup.html", {'form': form})
