from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact

# Create your views here.


def index(request):
    context = {
        "variable1": "twenty-one",
        "variable2": "twenty-two"
    }
    return render(request, 'index.html', context)
    # return HttpResponse("This is home page")


def about(request):
    return render(request, 'about.html', )
    # return HttpResponse("This is about page")


def services(request):
    return render(request, 'services.html', )
    # return HttpResponse("This is services page")


def contact(request):
    if request.method == "POST":
        firstName = request.POST.get('firstName')
        lastName = request.POST.get('lastName')
        inputEmail4 = request.POST.get('inputEmail4')
        floatingTextarea = request.POST.get('floatingTextarea')
        contact = Contact(firstName=firstName, lastName=lastName, inputEmail4=inputEmail4, floatingTextarea=floatingTextarea)
        contact.save(),

    return render(request, 'contact.html', )
    # return HttpResponse("This is contact page")
