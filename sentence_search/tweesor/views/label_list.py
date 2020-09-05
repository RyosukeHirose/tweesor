from ..models import Label
from django.views.generic import ListView
from django.views.generic.edit import FormView, ModelFormMixin
from ..forms import IndexForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages

class LabelList(ListView, ModelFormMixin):

    template_name = 'label_list.html'
    context_object_name = 'label_lists'
    model = Label
    paginate_by = 10
    form_class = IndexForm

    def get(self, request, *args, **kwargs):
        self.object = None
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = None
        self.object_list = self.get_queryset()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    # 投稿後の登録処理
    def form_valid(self, form):
        print('-----------in LabelList form valid-------------')
        label_name = self.request.POST['create_label']
        if label_name=="":
            print('no label_name')
            return self.form_invalid(form)
        else:
            form.instance.label_name = label_name
            form.instance.label_mark = '__{}__'.format(label_name)
            form.save()
            messages.info(self.request, "新規の種別を登録しました")

            return HttpResponseRedirect(reverse('tweesor:label_list', kwargs={'success_message': '新規の種別を登録しました'}))

    def form_invalid(self, form):
        messages.error(self.request, "新規登録する種別を入力してください")
        return super().form_invalid(form)