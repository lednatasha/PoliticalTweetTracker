"""
Definition of views.
"""

from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from app.models import Tweets
import twitter

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)

     # Saving tweet
    #test = Tweets(tweetId = 123, twitterHandle="@test", text="test tweet text", time=datetime.now())
    #test.save()

    # Retrieving all tweets
    #tmp = Tweets.objects.all()

    # Get tweets from a specific time
    #api = twitter.Api(consumer_key='6GIVbGqgV2BsN22s9B7eytL45',
    #              consumer_secret='NH0zEMKVaecWEr5g301hwonB2pr3hvNNzOR4WFgIfTX8CxY7RR',
    #              access_token_key='932125473563336709-GJXnxMVgJaNshrA0fH5vygVhnJjqnEb',
    #              access_token_secret='6UuK79j7uWWdtdnjzTjmITDZE2eFpQ6axO2vIU3YarJ4l')
 
    #temp = api.GetSearch(raw_query="q=twitter%20&result_type=recent&since=2014-07-19&count=100")
    #for tweet in temp:
    #    tmp234234 = Tweets(tweetId=tweet.id, twitterHandle=tweet.user.screen_name, text=tweet.text, time=datetime.fromtimestamp(tweet.created_at_in_seconds))
    #    tmp234234.save()

    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )
