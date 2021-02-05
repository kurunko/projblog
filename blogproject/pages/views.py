from topics.models import Thread, ThreadComment
from topics.forms import ThreadCommentForm
from django.views.generic.base import TemplateView

class HomePageView(TemplateView):
    template_name = "home/home.html"

    def get_context_data(self, **kwargs):
        kwargs['threads'] = Thread.objects.all

        return super().get_context_data(**kwargs)
    

