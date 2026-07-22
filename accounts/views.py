from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib import messages

User = get_user_model()


# ==========================
# Register
# ==========================
def register_view(request):

    if request.method == "POST":

        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        phone = request.POST.get("phone")
        gender = request.POST.get("gender")

        # Check username
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return redirect("register")

        # Check email
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists.")
            return redirect("register")

        # Check phone
        if User.objects.filter(phone=phone).exists():
            messages.error(request, "Phone number already exists.")
            return redirect("register")

        User.objects.create_user(
            username=username,
            email=email,
            password=password,
            phone=phone,
            gender=gender,
        )

        messages.success(request, "Registration Successful. Please Login.")
        return redirect("login")

    return render(request, "accounts/register.html")


# ==========================
# Login
# ==========================
def login_view(request):

    if request.user.is_authenticated:
        return redirect("home")

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            login(request, user)

            next_url = request.POST.get("next")

            if next_url:
                return redirect(next_url)

            return redirect("home")

        messages.error(request, "Invalid Username or Password")

    return render(request, "accounts/login.html")


# ==========================
# Logout
# ==========================
def logout_view(request):

    logout(request)

    messages.success(request, "Logged out successfully.")

    return redirect("login")