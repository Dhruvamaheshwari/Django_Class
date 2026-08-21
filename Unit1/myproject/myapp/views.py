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


# dynamic url
def dynamic_url(req, name):
    return HttpResponse(f"Hello {name} welcome to my website")


def menuitem(req , dis):
    items = {
        'suger' : "cost is 75",
        "mango" : "cost is 60",
        "chocolate" : "cost is 100"
    }

    if dis in items:
        result = items[dis];
    else:
        result = "item is not found"
    
    return HttpResponse(f"this is your item {result}");


# movies finder
def movies(req  ,mov):
    items = {
        "Robot" : "ticket movie is 200",
        "movie2" : "ticket movie is 500",
        "movie2" : "ticket movie is 700",
    }

    if(mov in items):
        result = items[mov];
    else:
        result = "not found";
    return HttpResponse(f"this is your movie {result}😁😁");

# query parameter
def recip(req):
    food = req.GET.get("food");
    return HttpResponse(f"recipe available for food {food}");

def add(req):
    val1 = req.GET.get('val1');
    val2 = req.GET.get('val2');
    result = int(val1) + int(val2);
    return HttpResponse(f"you ans is {result}")