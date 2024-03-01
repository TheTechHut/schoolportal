

# C# units/views.py
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Unit

class UnitListView(ListView):
    model = Unit
    template_name = 'units/unit_list.html'  # Create this template in the 'units' app

class UnitDetailView(DetailView):
    model = Unit
    template_name = 'units/unit_detail.html'  # Create this template in the 'units' app

