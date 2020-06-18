from django.shortcuts import render
from django.http import HttpResponse
from .item.tweet_get import tweet_get
from .item.text_changer import get_words_by_mecab
from .item.write_text import write_txt
from .models import LearnTweet, TemporaryData, Label
from .forms import IndexForm, SearchForm
from django.views.generic.edit import FormView, CreateView


class Index(FormView):
    template_name = 'index.html'
    model = Label
    success_url = "/"
    form_class = IndexForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print('in Index get_context_data')
        # ツイートの入れ物を用意してツイートを取得
        tweets_list = []
        tweets = TemporaryData.objects.all()
        for tweet in tweets:
            tweets_list.append((tweet.temp_text, tweet.temp_tweet_id))

        # Labelをセレクトボックスで表示するためタグを取得
        labels = Label.objects.all()
        

        context = {
            'tweets': tweets_list,
            'label_name': IndexForm(**self.get_form_kwargs())['label_name'],
            'labels': IndexForm(**self.get_form_kwargs())['labels']
            # 'search_form': SearchForm(),
        }
        return context
        
    # 投稿後の登録処理
    def form_valid(self, form):
        print('in Index form valid')
        label_name = form.instance.label_name
        print(label_name)
        form.instance.label_mark = '__{}__'.format(label_name)
        form.save()

        return super().form_valid(form)



def learn_tweet(request, tweet_id):
    if request.method == 'POST':
        print('in learn_tweet')
        a = IndexForm()
        
        print("------------------{}----------------".format(request.POST['labels']))
        # 一時保存から該当データを取得して整形
        target = TemporaryData.objects.filter(temp_tweet_id=tweet_id)
        target_word_list = get_words_by_mecab(target[0].temp_text)
        # fasttextに使うツイートを保存
        learn_tweet = LearnTweet.objects.update_or_create(
            tweet_id=tweet_id,
            text=target[0].temp_text,
            text_list=target_word_list,
        )
        # t extに書き込み
        write_txt(target_word_list)
    return HttpResponse('--ok--')

class SearchTweet(FormView):
    template_name = 'index.html'
    success_url = "/"
    form_class = IndexForm


    def form_valid(self, form):
        print('in form valid of SearchTweet')
        TemporaryData.objects.all().delete()
        searh_word = self.request.POST['search']
        tweets = tweet_get(searh_word)
        for tweet in tweets:
            temp_data = TemporaryData.objects.create(temp_tweet_id=tweet[1], temp_text=tweet[0])


        return super().form_valid(form)





    

