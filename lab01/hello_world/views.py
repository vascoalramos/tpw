from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def hello(request):
    return HttpResponse("Hello World!")


def number(request, num):
    resp = f"<html><body><h1>{num}</h1></body></html>"
    return HttpResponse(resp)


def number_2(request, num):
    params = {
        "num": num,
    }
    return render(request, "numbers_2.html", params)
