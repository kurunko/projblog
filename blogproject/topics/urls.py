from django.conf.urls import include
from django.urls import path
from django.urls.conf import re_path

from .views import ThreadListView, ThreadDetailView, ThreadCreateView

app_name = 'threads'

urlpatterns = [
    path('', ThreadListView.as_view(), name="threadList"),
    path('<str:game>/<str:category>/<str:slug>', ThreadDetailView.as_view(), name='threadDetail'),
    path('criar', ThreadCreateView.as_view(), name='threadCreate'),
    re_path(r'^chaining/', include('smart_selects.urls')),

]
