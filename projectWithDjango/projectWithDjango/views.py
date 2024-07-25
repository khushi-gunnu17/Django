from django.http import HttpResponse
from django.shortcuts import render


def home(request) :
    # return HttpResponse("Hello world. You are meeting Khushi Sharma at the home page.")

    # the file structure is mostly written beforehand.
    return render(request, 'website/index.html')

def about(request) :
    return render(request, 'website/about.html')

def contact(request) :
    return HttpResponse("Hello world. You are meeting Khushi Sharma at the contact page.")