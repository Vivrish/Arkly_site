from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('It\'s a list of items for sale')
# Create your views here.
