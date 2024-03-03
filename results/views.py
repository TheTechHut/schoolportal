from django.shortcuts import render
from django.views.generic import ListView
from .models import Result
# Create your views here.

class ResultListView(ListView):
    model = Result
    template_name = 'results/result_list.html'
    context_object_name = 'results'
