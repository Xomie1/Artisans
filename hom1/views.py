from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import SignUpForm
from . import views
from .models import SignUp, Login, Request, Feedback
from django.contrib.auth.hashers import make_password, check_password
from .models import Request,Feedback
from django.http import HttpResponseRedirect, JsonResponse, HttpResponseForbidden, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout







def artisan_homepage_view(request):
    return render(request, "artisanpage.html")


def user_homepage_view(request):
    return render(request, "Homepage.html")

def home_view(request):
    return render(request, "Home.html")



def logout_view(request):
    logout(request)
    return redirect('home')  # Redirect to home page after logout

def login(request):
    errors = {}

    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        role = request.POST['role']

        try:
            user = Login.objects.get(email=email)
            if check_password(password, user.password):
                if user.role == 'user':
                    # User has the 'user' role, redirect to user homepage
                    return redirect('user')
                elif user.role == 'artisan':
                    # User has the 'artisan' role, redirect to artisan homepage
                    return redirect('artisan')
            else:
                # Incorrect password
                errors['password'] = ["Incorrect password"]
        except Login.DoesNotExist:
            # User does not exist
            errors['email'] = ["User does not exist"]

    return render(request, 'user_management/login.html', {'errors': errors})





 




def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            # Hash the password before saving to the database
            password = form.cleaned_data['password']
            hashed_password = make_password(password)

            # Save data to SignUp table
            form.save()

            # Save data to Login table
            email = form.cleaned_data['email']
            role = request.POST['role']

            login_data = Login(email=email, password=hashed_password, role=role)
            login_data.save()

            # Redirect to login page after successful signup
            return redirect('login')
    else:
        form = SignUpForm()

    return render(request, 'user_management/signup.html', {'form': form})

def submit_request(request):
    if request.method == 'POST':
        artisan_name = request.POST.get('artisan_name')
        username = request.POST.get('username')
        phone_number = request.POST.get('phone_number')
        description = request.POST.get('description')

        new_request = Request(
            artisan_name=artisan_name,
            username=username,
            phone_number=phone_number,
            description=description,
        )
        new_request.save()

        return HttpResponseRedirect('/')

def submit_feedback(request):
    if request.method == 'POST':
        artisan_name = request.POST.get('artisan_name')
        username = request.POST.get('username')
        feedback = request.POST.get('feedback')

        new_feedback = Feedback(
            artisan_name=artisan_name,
            username=username,
            feedback=feedback,
        )
        new_feedback.save()

        return HttpResponseRedirect('/')


def get_artisans(request):
    artisans = SignUp.objects.filter(role='artisan').values('full_name', 'email', 'address', 'phone_number', 'profession')
    return JsonResponse({'artisans': list(artisans)})

def get_requests_and_feedback(request):
    full_name = request.GET.get('full_name')
    email = request.GET.get('email')

    requests_and_feedback = []

    if full_name and email:
        requests = Request.objects.filter(artisan_name=full_name)
        feedbacks = Feedback.objects.filter(artisan_name=full_name)  # Select feedback based on artisan_name

        for req in requests:
            requests_and_feedback.append({
                'description': req.description,
                'username': req.username,
                'phone_number': req.phone_number,
            })

        for fb in feedbacks:
            requests_and_feedback.append({
                'feedback': fb.feedback,
                'username': fb.username,
            })

    return JsonResponse({'requests_and_feedback': requests_and_feedback})






















