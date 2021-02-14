from ..models import LearnTweet, TemporaryData
from django.views.generic import ListView
from ..item.text_changer import get_words_by_mecab
from collections import Counter


class WordList(ListView):
    template_name = 'word_list.html'
    context_object_name = 'word_list'
    # paginate_by = 100

    def get_queryset(self):
        label_id = self.kwargs['label_id']
        learned_lists = LearnTweet.objects.filter(label=label_id)
        
        return learned_lists
        


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        label_id = self.kwargs['label_id']
        
        ver = self.kwargs['ver']
        if ver == 'neg':
            learned_lists = LearnTweet.objects.filter(label=label_id).filter(score__lt=0)
        else:
            learned_lists = LearnTweet.objects.filter(label=label_id)

        context['label_id'] = self.kwargs['label_id']
        wakachi_text_list = []

        for learned_list in learned_lists:
            wakachi_text_list = wakachi_text_list + get_words_by_mecab(learned_list.text).split()
            
        
        words_count = Counter(wakachi_text_list)
        sorted_words_count = dict(sorted(words_count.items(), key=lambda x:x[1], reverse=True))
        context['words_counts'] = sorted_words_count
        context['search_word'] = learned_lists[0].label
        print(ver)
        context['ver'] = ver

        return context       

class TempWordList(ListView):
    template_name = 'word_list.html'
    context_object_name = 'TemporaryData'
    # paginate_by = 100

    def get_queryset(self):

        learned_lists = TemporaryData.objects.all()
        
        return learned_lists
        


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
 
        learned_lists = TemporaryData.objects.all()

        wakachi_text_list = []

        for learned_list in learned_lists:
            wakachi_text_list = wakachi_text_list + get_words_by_mecab(learned_list.temp_text).split()
            
        
        words_count = Counter(wakachi_text_list)
        sorted_words_count = dict(sorted(words_count.items(), key=lambda x:x[1], reverse=True))
        context['words_counts'] = sorted_words_count
        context['search_word'] = "temp"
        return context  