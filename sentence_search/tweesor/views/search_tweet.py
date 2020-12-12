from ..item.tweet_get import tweet_get
from ..models import TemporaryData, LearnTweet, Label
from django.views.generic.edit import FormView
from ..forms import IndexForm
from ..item.text_changer import get_words_by_mecab

from datetime import datetime as dt
from pytz import timezone


class SearchTweet(FormView):
    template_name = 'index.html'
    success_url = "/"
    form_class = IndexForm


    def form_valid(self, form):
        try:
            # 前回の検索ツイートを初期化
            TemporaryData.objects.all().delete()
            searh_word = self.request.POST['search']
            tweets = tweet_get(searh_word)
            # すでに登録されているツイートを取得
            learn_tweets = LearnTweet.objects.all()

            for tweet in tweets:
                temp_time = dt.strptime(tweet[3], '%a %b %d %X %z %Y').astimezone(timezone('Asia/Tokyo'))
                time = temp_time.strftime('%Y年%m月%d日 %H時%M分')
                temp_data = TemporaryData.objects.create(
                    temp_tweet_id=tweet[1], 
                    temp_text=tweet[0], 
                    temp_location=tweet[2], 
                    temp_iine = tweet[5],
                    temp_retweet = tweet[6],
                    temp_created_at=time,
                    search_word=searh_word,
                    temp_user_name = tweet[7],
                    temp_follow = tweet[8],
                    temp_followers = tweet[9])
                
                label=Label.objects.update_or_create(
                    label_name=searh_word)

                learn_data=LearnTweet.objects.update_or_create(
                    tweet_id=tweet[1],
                    text=tweet[0],
                    iine_count=tweet[5],
                    retweet_count=tweet[6],
                    created_at=time,
                    label=Label.objects.filter(label_name=searh_word)[0],
                    user_name = tweet[7],
                    follow = tweet[8],
                    followers = tweet[9]
                    )

            

            return super().form_valid(form)

        except TypeError:
            return super().form_invalid(form)
    
    def form_invalid(self, form):
        return super().form_invalid(form)

        