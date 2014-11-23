from django.http.response import HttpResponse
from django.shortcuts import render_to_response
from models import NewsFeedPost
from django.contrib.auth.models import User


def home(request):
    context = {"users": User.objects.all(),
               "news_feed_posts": NewsFeedPost.objects.all(),
               }
    return render_to_response("index.html", context)


def users(request):
    return HttpResponse("this is the users page")

def habit_input(request):
    return HttpResponse("Please enter your habit")

