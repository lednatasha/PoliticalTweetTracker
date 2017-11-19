"""
Definition of models.
"""

from django.db import models

# Create your models here.
class Tweets(models.Model):
    id = models.IntegerField(primary_key=True)
    twitterHandle = models.CharField(max_length=50)
    tweetId = models.BigIntegerField()
    text = models.CharField(max_length=360)
    time = models.DateTimeField()