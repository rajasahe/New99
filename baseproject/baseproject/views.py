from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, "index.html")

def contact(request):
    return render(request, "contact.html")

def results(request):
    value = request.GET["txt"]
    value = value + " added text in Python"
    return render(request, "results.html", {"val":value})
