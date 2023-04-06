from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import ToDoForm

# Create your views here.

class FeedView(TemplateView):

    template_name = "feed/feed.html"
    form_class = ToDoForm
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ToDoForm()
        return context
