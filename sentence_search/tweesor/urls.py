from django.urls import path
from . import views
app_name = 'tweesor'

urlpatterns = [
    
    path('learn/<int:tweet_id>/', views.learn_tweet, name='learn'),
    path('search_tweet/', views.SearchTweet.as_view(), name='search_tweet'),
    path('', views.Index.as_view(), name='index'),
    # path('upload/', views.upload.Upload.as_view(), name='upload'),


]
