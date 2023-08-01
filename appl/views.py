from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from .models import Profile, Transactions


def dashboard_view(request):
    transactions = Transactions.objects.filter(user=request.user)
    profiles = Profile.objects.filter(user=request.user)
    context = {
        'transactions': transactions,
        'profiles': profiles}
    template = 'cooladmin/index.html'
    return render(request, template, context)


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                messages.info(request, f"you are now logged in as {username}.")
                return redirect("/")
            else:
                messages.error(request, "invalid username or password")
        else:
            messages.error(request, "invalid username or password")
    form = AuthenticationForm()
    template = 'login_index.html'
    return render(request=request, template_name=template, context={"login_form": form})


def logout_view(request):
    logout(request)
    messages.info(request, "you have successfully logged out. ")
    return redirect("/login/")

