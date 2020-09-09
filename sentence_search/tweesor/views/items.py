from django.http import HttpResponseRedirect, HttpResponse

# from ..item.text_changer import get_words_by_mecab
from ..item.write_text import write_txt
from ..models import LearnTweet, TemporaryData, Label
from ..forms import IndexForm
from django.views.generic.edit import FormView
from django.shortcuts import redirect, render
from django.urls import reverse

import urllib
import csv

# def learn_tweet(request, tweet_id):
#     """
#     ツイートを記憶させるメソッド
#     """
#     if request.method == 'POST':
        
#         print('----------in learn_tweet----------')
#         try:
#             label = Label.objects.filter(label_mark=request.POST['labels'])

#             # 一時保存から該当データを取得して整形
#             target = TemporaryData.objects.filter(temp_tweet_id=tweet_id)
#             target_word_list = get_words_by_mecab(target[0].temp_text)
#             # fasttextに使うツイートを保存
#             learn_tweet = LearnTweet.objects.update_or_create(
#                 tweet_id=tweet_id,
#                 text=target[0].temp_text,
#                 text_list=target_word_list,
#                 label=label[0]
#             )
#             # textに書き込み
#             write_txt(target_word_list, request.POST['labels'])

#         except (KeyError, Label.DoesNotExist):
#             # Redisplay the question voting form.
#             return HttpResponseRedirect(reverse('tweesor:index', kwargs={'error_message': 'error 予期せぬエラーが発生しました'}))
            
#         except IndexError:
#             return HttpResponseRedirect(reverse('tweesor:index', kwargs={'error_message': 'error 種別を選択してください'}))
#         else:

#             return HttpResponseRedirect(reverse('tweesor:index', kwargs={'post_message': 'success ツイートを学習しました'}))

def delete_tweet(request, label_id, tweet_id):
    if request.method == 'POST':
        
        print('----------in delete_tweet----------')
        try:
            LearnTweet.objects.filter(tweet_id=tweet_id).filter(label=label_id)[0].delete()

            
        except:
            return HttpResponseRedirect(reverse('tweesor:learn_tweet', kwargs={'error_message': 'error 削除に失敗しました'}))
        else:

            return HttpResponseRedirect(reverse('tweesor:learn_tweet', kwargs={'label_id':label_id, 'post_message': 'success　学習したツイートを削除しました'}))

def post_export(request):
    """
    役職テーブルを全件検索して、CSVファイルを作成してresponseに出力します。
    """
    response = HttpResponse(content_type='text/csv; charset=UTF-8')
    filename = urllib.parse.quote((u'{}.csv'.format(TemporaryData.objects.all()[0].search_word)).encode("utf8"))
    response['Content-Disposition'] = 'attachment; filename*=UTF-8\'\'{}'.format(filename)
    writer = csv.writer(response)
    writer.writerow(['検索語句', '時間', 'location', '本文'])
    for data in TemporaryData.objects.all():
        writer.writerow([data.search_word, data.temp_created_at, data.temp_location, data.temp_text])
    return response