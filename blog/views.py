from django.shortcuts import render, HttpResponse
from django.views import generic
# Create your views here.

class IndexView(generic.ListView):
    template_name='blog/post_list.html'

    def get_queryset(self):
        return 'Hello World..!'

