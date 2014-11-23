from django.http.response import HttpResponse
from django.shortcuts import render_to_response


def home(request):
    return render_to_response("index.html")


def users(request):
    return HttpResponse("this is the users page")