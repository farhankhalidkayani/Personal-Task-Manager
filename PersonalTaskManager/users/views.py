from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def index(request):
    return redirect("tasks:task_list")


def register_user(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = UserCreationForm()
    return render(request, "register.html", {"form": form})
