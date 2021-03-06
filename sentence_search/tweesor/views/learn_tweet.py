from ..models import LearnTweet
from django.views.generic import ListView


class LearnedTweet(ListView):

    template_name = 'learn_tweet.html'
    context_object_name = 'learn_tweets'
    paginate_by = 100

    def get_queryset(self):
        label_id = self.kwargs['label_id']
        learned_list = LearnTweet.objects.filter(label=label_id).order_by('-created_at')
        if 'order' in self.kwargs:
            order = self.kwargs['order']
            if order == 'iine':
                learned_list = learned_list.order_by('-iine_count')
            elif order == 'follower':
                learned_list = learned_list.order_by('-followers')
                





        return learned_list

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        learned_list = LearnTweet.objects.filter(label=self.kwargs['label_id'])
        total_number = len(learned_list)

        context['label_id'] = self.kwargs['label_id']
        context['total_number'] = total_number
        if 'post_message' in self.kwargs:
            message = 'error_message' if 'error' in  self.kwargs['post_message'] else 'post_message'
            context[message] = self.kwargs['post_message']

            return context       
        else:
            return context

