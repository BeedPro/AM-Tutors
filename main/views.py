from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, "home.html", {})

def about(request):
    return render(request, "about.html", {"title": "About Us"})

def tuition(request):
    return render(request, "tuition.html", {"title": "Tuition"})

def reviews(request):
    return render(request, "reviews.html", {"title": "Reviews"})

def pricing(request):
    return render(request, "pricing.html", {"title": "Pricing"})

def contacts(request):
    return render(request, "contacts.html", {"title": "Contacts"})