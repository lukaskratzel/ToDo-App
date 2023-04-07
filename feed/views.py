from django.shortcuts import render
from django.views.generic import FormView, ListView, View
from django.http import JsonResponse, HttpResponseBadRequest
from .forms import ToDoForm
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import ToDo

# Create your views here.

class FeedView(FormView, ListView):

    template_name = "feed.html"
    form_class = ToDoForm
    success_url = "/"
    context_object_name = "todos"
    
    def dispatch(self, request, *args, **kwargs):
        self.request = request
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return ToDo.objects.filter(user=self.request.user).order_by('-priority')
        else:
            return ToDo.objects.none()
        
    def form_valid(self, form):
        if self.request.user.is_authenticated:
            ToDo.objects.create(
                text=form.cleaned_data['text'],
                priority=form.cleaned_data['priority'],
                user=self.request.user
            )
            return super().form_valid(form)
        else:
            return None
        
class DeleteView(LoginRequiredMixin, View):

    http_method_names = ['post']

    def post(self, request, *args, **kwargs):
        data = request.POST.dict()

        if 'id' not in data:
            return HttpResponseBadRequest('Missing data')
        
        try:
            if ToDo.objects.filter(id=data['id']) and ToDo.objects.get(id=data['id']).user != request.user:
                raise Exception
        except:
            return HttpResponseBadRequest('Illegal request')
        
        ToDo.objects.get(id=data['id']).delete()
        return JsonResponse({
            'success': True
        })
        
        
            


