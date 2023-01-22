from django.shortcuts import render
from django.shortcuts import render
from .forms import ContactForm

# Create your views here.



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
