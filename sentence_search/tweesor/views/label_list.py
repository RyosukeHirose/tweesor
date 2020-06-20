from ..models import Label
from django.views.generic import ListView


class LabelList(ListView):

    template_name = 'label_list.html'
    context_object_name = 'label_lists'
    model = Label
    paginate_by = 10