from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def australia(request):
    return render(request,'australia.html')

def swan(request):
    return HttpResponse("Welcome Good morning")