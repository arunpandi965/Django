from django.shortcuts import render

def home (request):
    context={}
    return render(request, "ITPTApp/home.html", context)

def dashboard (request):
    context={}
    return render(request, "ITPTApp/dashboard.html", context)
