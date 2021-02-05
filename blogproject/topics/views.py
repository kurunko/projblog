# Standard Python Library imports.
from functools import reduce
import operator

# Core Django imports.
from django.contrib import messages
from django.db.models import Q, Count
from django.views.generic import (
    DetailView,
    ListView,
)
from django.views.generic.edit import CreateView, UpdateView


# Blog application imports.
from .models import (
                        Thread, 
                        ThreadCategory, 
                        ThreadComment
    )
from .forms import (
                        ThreadCommentForm,
                        ThreadCreateForm
    )
from django.http import HttpResponseRedirect

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseForbidden
from django.views.generic.edit import FormMixin






class ThreadListView(ListView):
    context_object_name = "threads"
    paginate_by = 25
    queryset = Thread.objects.filter(flagged=False)
    template_name = "thread/threadlist.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = ThreadCategory.objects.all()
        return context


class ThreadDetailView(FormMixin, DetailView):
    model = Thread
    template_name = 'thread/threaddetail.html'
    form_class = ThreadCommentForm
    success_url = "#"

    def get_context_data(self, **kwargs):
        session_key = f"viewed_article {self.object.slug}"
        if not self.request.session.get(session_key, False):
            self.object.views += 1
            self.object.save()
            self.request.session[session_key] = True
        


        kwargs['article'] = self.object
        kwargs['comment_form'] = ThreadCommentForm()
        kwargs['comments'] = ThreadComment.objects.filter(flagged=False).filter(thread__id=self.object.id)
        return super().get_context_data(**kwargs)

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseForbidden()
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.thread = get_object_or_404(Thread,
                                            slug=self.kwargs.get('slug'))
        comment.save()
        messages.success(self.request, "Comment Added successfully")
        return HttpResponseRedirect(self.request.path_info)

class ThreadCreateView(CreateView):
    model = Thread
    form_class = ThreadCreateForm
    template_name = 'thread/threadcreate.html'


class ThreadEditView(UpdateView):
    model = Thread
    form_class = ThreadCreateForm
    template_name = 'thread/threadedit.html'

    def get_object(self):
            return Thread.objects.get(slug=self.kwargs['slug'])