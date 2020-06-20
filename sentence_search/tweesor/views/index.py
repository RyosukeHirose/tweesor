from ..models import TemporaryData, Label
from ..forms import IndexForm
from django.views.generic.edit import FormView

class Index(FormView):
    template_name = 'index.html'
    model = Label
    success_url = "/"
    form_class = IndexForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print('----------in Index get_context_data----------')
        # ツイートの入れ物を用意してツイートを取得
        tweets_list = []
        tweets = TemporaryData.objects.all()
        for tweet in tweets:
            tweets_list.append((tweet.temp_text, tweet.temp_tweet_id))

        form = IndexForm()
        context = {
            'tweets': tweets_list,
            'create_label': form['create_label'],
            'labels': form['labels'] ,
        }
        return context

    # 投稿後の登録処理
    def form_valid(self, form):
        print('-----------in Index form valid-------------')
        label_name = self.request.POST['create_label']
        form.instance.label_name = label_name
        form.instance.label_mark = '__{}__'.format(label_name)
        form.save()

        return super().form_valid(form)
    
