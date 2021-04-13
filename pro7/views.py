from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return HttpResponse("<h1>hello,welcome to views of pro7</h1>")
def index2(request):
    return render(request,"home.html")