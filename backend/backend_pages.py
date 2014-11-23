from django.http.response import HttpResponse
from django.shortcuts import render_to_response
from models import NewsFeedPost
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate
from django.core.context_processors import csrf

def home(request):
    context = {"users": User.objects.all(),
               "news_feed_posts": NewsFeedPost.objects.all(),
               }
    context.update(csrf(request))
    return render_to_response("index.html", context)


def users(request):
    return HttpResponse("this is the users page")

def habit_input(request):
    return HttpResponse("Please enter your habit. Do you want to break or form this habit?")

def habit(request):
    return HttpResponse("Now let's break or form this habit!")

def login(request):
    return render_to_response("login.html")

def loginhandler(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return reverse("home")
            # Redirect to a success page.
        else:
            # Return a 'disabled account' error message
            pass
    else:
        # Return an 'invalid login' error message.
        return HttpResponse("This account does not exist! Create one here!")
    