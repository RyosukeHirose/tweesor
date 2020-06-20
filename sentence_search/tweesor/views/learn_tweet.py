from ..models import LearnTweet
from django.views.generic import ListView


class LearnedTweet(ListView):

    template_name = 'learn_tweet.html'
    context_object_name = 'learn_tweets'
    paginate_by = 20

    def get_queryset(self):
        label_id = self.kwargs['label_id']
        learned_list = LearnTweet.objects.filter(label=label_id)
        print(learned_list)


        return learned_list
