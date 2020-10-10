from ..models import LearnTweet
from django.views.generic import ListView


class LearnedTweet(ListView):

    template_name = 'learn_tweet.html'
    context_object_name = 'learn_tweets'
    paginate_by = 100

    def get_queryset(self):
        label_id = self.kwargs['label_id']
        learned_list = LearnTweet.objects.filter(label=label_id)
        print(learned_list)


        return learned_list

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print('----------in Index get_context_data----------')
        context['label_id'] = self.kwargs['label_id']
        if 'post_message' in self.kwargs:
            message = 'error_message' if 'error' in  self.kwargs['post_message'] else 'post_message'
            context[message] = self.kwargs['post_message']

            return context       
        else:
            return context

