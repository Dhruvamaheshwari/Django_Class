from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def hello(request):
    name = "Dhruva Maheshwari"
    return HttpResponse(f"Hello my name is {name}")

def home(req):
    return HttpResponse('<h1 style="color:blue" >Welcome to the Home page</h1>')

def about(req):
    return HttpResponse('This is the about page')


def result(req):
    mark = 60
    if(mark < 50):
        return HttpResponse("not Good")
    elif(mark >= 50 and mark <=70):
        return HttpResponse("good")
    elif(mark >= 70 and mark <=90):
        return HttpResponse("Excellent")
    else:
        return HttpResponse("very Excellent")
    