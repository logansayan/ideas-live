from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .forms import CustomUserCrationFrom

# Create your views here.

def loginUser(request):
  # If user is already logged in
  if request.user.is_authenticated:
    return redirect("all_notes")

  # Login User
  if request.method == "POST":
    username = request.POST["username"]
    password = request.POST["password"]
    
    # user = User.objects.get(username=username)

    user = authenticate(request, username=username, password=password)

    if user is not None:
      login(request, user)
      return redirect("all_notes")
    else:
      messages.error(request, "Username or password is incorrect!")

  return render(request, "users/register_login.html")

def registerUser(request):
  page = "register"
  form = CustomUserCrationFrom()
  if request.method == "POST":
    form = CustomUserCrationFrom(request.POST)
    
    if form.is_valid():
      user = form.save(commit=False)
      user.username = user.username.lower()
      user.save()
      messages.success(request, "User account was created!")

      login(request, user)
      return redirect("all_notes")

    else:
      messages.debug("An error has occurred during registration!")
  context = {
    "page": page,
    "form": form
  }

  return render(request, "users/register_login.html", context)

def logoutUser(request):
  logout(request)
  messages.info(request, "User was logged out!")
  return redirect("login")