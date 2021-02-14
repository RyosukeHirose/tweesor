from ..models import LearnTweet
from django.views.generic import ListView
from google.cloud import language_v1
from ..item.sample_analyze_entity_sentiment import sample_analyze_sentiment

class EmotionalCheck(ListView):

    template_name = 'learn_tweet.html'
    context_object_name = 'learn_tweets'
    paginate_by = 100


    def get_queryset(self):
        import os
        os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '../emotional-check-0d3ec3f32480.json'
        label_id = self.kwargs['label_id']
        learned_lists = LearnTweet.objects.filter(label=label_id).order_by('-created_at')
        # for learned_list in learned_lists:
        #     entitis = sample_analyze_entity_sentiment(learned_list.text)
        # entitis = sample_analyze_entity_sentiment('最近天気が悪くて洗濯物が干せず、深夜にコインランドリーに通う羽目になり睡眠不足気味で辛い。')
        return learned_lists


    # def get_queryset(self):
    #     label_id = self.kwargs['label_id']
    #     learned_list = LearnTweet.objects.filter(label=label_id).order_by('-created_at')
    #     if 'order' in self.kwargs:
    #         order = self.kwargs['order']
    #         if order == 'iine':
    #             learned_list = learned_list.order_by('-iine_count')
    #         elif order == 'follower':
    #             learned_list = learned_list.order_by('-followers')
            
    #     return learned_list

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        learned_lists = LearnTweet.objects.filter(label=self.kwargs['label_id'])
        total_number = len(learned_lists)
        responses = []
        temp_scores = []
        scores = []
        count = 0
        count2 = 0
        roop = 10
        print('ネガポジチェックスタート')
        for learned_list in learned_lists:
            if count > roop:
                aaa = 111
            elif learned_list.score == None:
                print('チェックスタート')
                check_responses = sample_analyze_sentiment(learned_list.text)
                responses.append(check_responses)
                count = count + 1
            else:               
                print('もうある')
                responses.append(learned_list.score)
        for learned_list, response in zip(learned_lists,responses):
            if count2 > roop:
                aaa = 111
            elif learned_list.score == None:
                print('---------------------')
                print(response.document_sentiment.score)
                # for sentence in response.sentences:
                #     scores.append(sentence.sentiment.score)
                #     LearnTweet.objects.filter(text=learned_list.text).update(score=sentence.sentiment.score)
                scores.append(response.document_sentiment.score)
                LearnTweet.objects.filter(text=learned_list.text).update(score=response.document_sentiment.score)
                count2 = count2 + 1
                print('データ更新')
            else:

                scores.append(response)

        if self.kwargs['ver'] == 'neg':
            copy_learned_lists = learned_lists
            copy_scores = scores
            learned_lists = []
            scores = []
            for copy_learned_list, copy_score in zip(copy_learned_lists, copy_scores):

                if copy_score < 0:
                    learned_lists.append(copy_learned_list)
                    scores.append(copy_score)
    # print(sentences[0].sentiment.score)
        # print(sentences[0].sentiment.magnitude)


        context['learn_tweets'] = learned_lists
        context['scores'] = scores
        context['ver'] = self.kwargs['ver']
        context['label_id'] = self.kwargs['label_id']
        context['total_number'] = total_number
        if 'post_message' in self.kwargs:
            message = 'error_message' if 'error' in  self.kwargs['post_message'] else 'post_message'
            context[message] = self.kwargs['post_message']

            return context       
        else:
            return context
