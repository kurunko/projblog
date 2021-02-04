from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.http.response import HttpResponseForbidden, HttpResponseRedirect
from django.urls.base import reverse_lazy
from django.views import generic
from django.views.generic import CreateView
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormMixin
from django.views.generic.list import ListView




from .models import CustomUser
from topics.models import ThreadComment, Thread
from topics.forms import ThreadCommentForm

from .forms import CustomUserCreationForm, FlagAsSpamForm, UserUpdateForm

def CustomUserCreationView(request):
    context = {}
    if request.POST:
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(email=email, password=raw_password)
            login(request, account)
            return redirect('home')
        else:
            context['registration_form'] = form
    else:
        form = CustomUserCreationForm()
        context['registration_form'] = form
    return render(request, 'user/registro/criarUser.html', context)


class CustomUserLoginView(SuccessMessageMixin, LoginView):
    template_name = 'user/entrar/entrar.html'
    success_url = '/'
    success_message = "You were successfully logged in"




class CustomUserUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = CustomUser
    form_class = UserUpdateForm
    success_url = reverse_lazy('home')
    template_name = 'user/update/update.html'

    def get_object(self):
            return self.request.user

    
class ManageView(ListView):
    context_object_name = "comments"
    queryset = ThreadComment.objects.all()
    template_name = "user/adm/manage.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context



class MarkAsSpamView(LoginRequiredMixin, generic.UpdateView):
    model = ThreadComment
    template_name = 'user/adm/markasspam.html'
    fields = ['flagged']
    success_url = "/noticias"
    pk_field = 'id'
    pk_url_kwarg = 'id'

    def get_object(self):
            return self.request.user