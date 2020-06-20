from django.http import HttpResponse
from ..item.text_changer import get_words_by_mecab
from ..item.write_text import write_txt
from ..models import LearnTweet, TemporaryData, Label
from ..forms import IndexForm
from django.views.generic.edit import FormView

def learn_tweet(request, tweet_id):
    if request.method == 'POST':
        print('----------in learn_tweet----------')
        print(request.POST['labels'])
        label = Label.objects.filter(label_mark=request.POST['labels'])
        # 一時保存から該当データを取得して整形
        target = TemporaryData.objects.filter(temp_tweet_id=tweet_id)
        target_word_list = get_words_by_mecab(target[0].temp_text)
        # fasttextに使うツイートを保存
        learn_tweet = LearnTweet.objects.update_or_create(
            tweet_id=tweet_id,
            text=target[0].temp_text,
            text_list=target_word_list,
            label=label[0]
        )
        # textに書き込み
        write_txt(target_word_list, request.POST['labels'])
    return HttpResponse('--ok--')