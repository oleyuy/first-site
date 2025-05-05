from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    context = {
        'name': 'Oleh',
        'age' : 19
    }
    return render(request,"home/home.html",context)
# Create your views here.
