from django.db import models
from django.utils import timezone

class Label(models.Model):
    label_name = models.CharField(default="", max_length=128)
    label_mark = models.CharField(default="", max_length=128)
 
    def __str__(self):
        return self.label_name

class LearnTweet(models.Model):
    tweet_id = models.IntegerField(default='')
    text = models.TextField(default='')
    text_list = models.TextField(default='')
    created_at = models.TextField(default='')
    location = models.TextField(default='')
    iine_count = models.IntegerField(blank=True, null=True)
    retweet_count = models.IntegerField(blank=True, null=True)
    user_name = models.TextField(default='')
    follow = models.IntegerField(blank=True, null=True)
    followers = models.IntegerField(blank=True, null=True)

    label = models.ForeignKey(
        Label,
        default = '',
        on_delete=models.CASCADE,
        related_name = "tweets"
        )
    score = models.FloatField(blank=True, null=True)


    def __str__(self):
        return str(self.text)



class TemporaryData(models.Model):
    temp_tweet_id = models.IntegerField()
    temp_text = models.TextField()
    temp_created_at = models.TextField(default='')
    temp_location = models.TextField(default='')
    search_word = models.TextField(default='')
    temp_iine = models.IntegerField(blank=True, null=True)
    temp_retweet = models.IntegerField(blank=True, null=True)
    temp_user_name = models.TextField(default='')
    temp_follow = models.IntegerField(blank=True, null=True)
    temp_followers = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.temp_text


    