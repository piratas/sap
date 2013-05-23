#encoding: utf-8

from django.shortcuts import (render, get_object_or_404, 
    redirect)
from .models import Voluntarios
from django.core.paginator import (Paginator, PageNotAnInteger,
    EmptyPage)
from django.views.generic.base import RedirectView

from forms import GTIForm


def index(request):
    template_name = 'voluntarios/index.html'
    context = {}
    return render(request, template_name, context)

def gti(request):
    template_name = 'voluntarios/gti.html'
    context = {}

    if request.method == 'POST':
        form = GTIForm(request.POST)
        if form.is_valid():
            voluntario = form.save()
            context['success'] = True

    else:
        form = GTIForm()
    
    context['form'] = form

    return render(request, template_name, context)