from django.urls import path
from . import views
app_name = 'tweesor'

urlpatterns = [
    
    path('learn/<int:tweet_id>/', views.items.learn_tweet, name='learn'),
    path('search_tweet/', views.search_tweet.SearchTweet.as_view(), name='search_tweet'),
    path('', views.index.Index.as_view(), name='index'),
    path('<str:post_message>', views.index.Index.as_view(), name='index'),
    path('<str:error_message>', views.index.Index.as_view(), name='index'),
    path('label_list/', views.label_list.LabelList.as_view(), name='label_list'),
    path('label_list/<str:success_message>/', views.label_list.LabelList.as_view(), name='label_list'),
    path('learn_tweet/<int:label_id>', views.learn_tweet.LearnedTweet.as_view(), name='learn_tweet'),
    path('learn_tweet/<int:label_id>/<str:post_message>/', views.learn_tweet.LearnedTweet.as_view(), name='learn_tweet'),
    path('delete_tweet/<int:label_id>/<int:tweet_id>', views.items.delete_tweet, name='delete_tweet'),
    path('export/', views.items.post_export, name='export'),
    # path('check_tweet', views.check_tweet.CheckTweet.as_view(), name='check_tweet'),
    # path('upload/', views.upload.Upload.as_view(), name='upload'),


]
