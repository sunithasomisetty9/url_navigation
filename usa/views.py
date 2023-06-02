from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def europe(request):
    return render(request,'europe.html')

def peacock(request):
    return HttpResponse("peacock is national bird")
