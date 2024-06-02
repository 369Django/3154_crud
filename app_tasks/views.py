from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def h(request):
    c=6+6
    return HttpResponse('El ressultado es  ',c)

