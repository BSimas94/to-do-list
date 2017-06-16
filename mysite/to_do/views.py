from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.views.generic import TemplateView,ListView,CreateView,DeleteView
from . import models

# Create your views here.
class IndexView(TemplateView):
    template_name = 'index.html'

class TaskListView(ListView):
    model = models.Task
    template_name = 'task/task_list.html'

class TaskCreateView(CreateView):
    fields = ('name','description')
    model = models.Task

class TaskDeleteView(DeleteView):
    model = models.Task
    success_url = reverse_lazy('to_do:list')
