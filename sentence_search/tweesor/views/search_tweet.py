from ..item.tweet_get import tweet_get
from ..models import TemporaryData
from django.views.generic.edit import FormView
from ..forms import IndexForm


class SearchTweet(FormView):
    template_name = 'index.html'
    success_url = "/"
    form_class = IndexForm


    def form_valid(self, form):
        print('-----------in form valid of SearchTweet------------')
        TemporaryData.objects.all().delete()
        searh_word = self.request.POST['search']
        tweets = tweet_get(searh_word)
        for tweet in tweets:
            temp_data = TemporaryData.objects.create(temp_tweet_id=tweet[1], temp_text=tweet[0])

        return super().form_valid(form)
    
    def form_invalid(self, form):
        print('aaaaaaa')
        return super().form_invalid(form)