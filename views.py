from django.shortcuts import render,redirect
from django.http import HttpResponse
from portfolioapp.models import Contact
from portfolioapp.form import ContactForm


# Create your views here.
def index(request):
    return HttpResponse("<h1 style= 'color:red; text-align:center'>welcome to django!  </h1>")

def portfolio(request):
    return render(request,"portfolio.html")
    
def contact(request):
    sform=ContactForm()
    if request.method=="POST":
        sform=ContactForm(request.POST)
        if sform.is_valid():
            sform.save()
            return redirect ("/portfolio")
    else:
        return render(request,"contact.html",{'sform':sform})
        



