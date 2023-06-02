from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def parrot(request):
    return HttpResponse("Hi Good morning!!!")


def canada(request):
    return render(request,'canada.html')