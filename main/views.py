from django.http import BadHeaderError, HttpResponse
from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import send_mail
# Create your views here.
# Think of this as controllers in ASP.NET

def send_email(name, email, message):
    try:
        send_mail(
            'Contact Us Email',
            f'Here is the message. {message}',
            f'{email}',
            ['annoor.tutor@outlook.com'],
            fail_silently=False
            )
    except BadHeaderError:
        return HttpResponse('Invalid header found.')
    return redirect('success')


def home(request):
    is_home_page = request.path == '/'
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            pass
    return render(request, 'home.html', {"title": "Home page", 'form': form, 'is_home_page': is_home_page})

def about(request):
    return render(request, "about.html", {"title": "About Us"})

def tuition(request):
    return render(request, "tuition.html", {"title": "Tuition"})

def reviews(request):
    return render(request, "reviews.html", {"title": "Reviews"})

def pricing(request):
    return render(request, "pricing.html", {"title": "Pricing"})

def contacts(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            pass
    return render(request, 'contacts.html', {"title": "Contact Us", 'form': form})

def success(request):
    return render(request, "success.html", {"title" : "Success"})

def gcse(request):
    return render(request, "gcse.html", {"title": "GCSE"})

def alevel(request):
    return render(request, "alevel.html", {"title": "A-Levels"})

def step(request):
    return render(request, "step.html", {"title": "STEP"})

def programming(request):
    return render(request, "programming.html", {"title": "Programming"})
