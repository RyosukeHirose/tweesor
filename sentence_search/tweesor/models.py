from django.db import models
from django.utils import timezone

class Label(models.Model):
    label_name = models.CharField(default="", max_length=128)
    label_mark = models.CharField(default="", max_length=128)
 
    def __str__(self):
        return self.label_name

class LearnTweet(models.Model):
    tweet_id = models.IntegerField()
    text = models.TextField()
    text_list = models.TextField()
    label = models.ForeignKey(
        Label,
        default = '',
        on_delete=models.CASCADE,
        related_name = "tweets"
        )


    def __str__(self):
        return str(self.tweet_id)



class TemporaryData(models.Model):
    temp_tweet_id = models.IntegerField()
    temp_text = models.TextField()

    def __str__(self):
        return self.temp_text


    