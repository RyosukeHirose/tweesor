from ..models import TemporaryData, Label
from ..forms import IndexForm
from django.views.generic.edit import FormView, ModelFormMixin
from django.views.generic import ListView
from ..item.text_changer import get_words_by_mecab

from collections import Counter

class Index(ListView, ModelFormMixin):
    template_name = 'index.html'
    model = TemporaryData
    context_object_name = 'tweets'
    success_url = "/"
    form_class = IndexForm
    paginate_by = 10


    def get(self, request, *args, **kwargs):
        self.object = None
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        print('post')
        self.object = None
        self.object_list = self.get_queryset()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:   
            return self.form_invalid(form)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print('----------in Index get_context_data----------')
        tweets = TemporaryData.objects.all()
        wakachi_text_list = []

        for tweet in tweets:
            wakachi_text_list = wakachi_text_list + get_words_by_mecab(tweet.temp_text).split()
            
        
        words_count = Counter(wakachi_text_list)
        sorted_words_count = dict(sorted(words_count.items(), key=lambda x:x[1], reverse=True))
        print("---------{}--".format(sorted_words_count))
        context['words_counts'] = sorted_words_count
        if 'post_message' in self.kwargs:
            message = 'error_message' if 'error' in  self.kwargs['post_message'] else 'post_message'
            context[message] = self.kwargs['post_message']

            return context       
        else:
            return context


