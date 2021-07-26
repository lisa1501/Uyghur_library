from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return HttpResponse('<hi>Blog Home<hi/>')

def about(request):
    return HttpResponse('<hi>Blog About<hi/>')