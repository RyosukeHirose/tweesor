from django.contrib import admin

# Register your models here.
from tweesor.models import Label, LearnTweet,TemporaryData
admin.site.register(Label)
admin.site.register(LearnTweet)
admin.site.register(TemporaryData)
