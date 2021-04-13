from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def print1(request):
    return HttpResponse("<h>this is the message from print1 method</h1>")
def print2(request,name,age,phone_num):
    return render(request,"home.html",context={"ename":name,"eage":age,"e_mobile":phone_num})