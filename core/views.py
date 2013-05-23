#encoding: utf-8

from django.shortcuts import render, redirect, render_to_response, HttpResponseRedirect, get_object_or_404

def home(request):
    context = {}
    
    return render(request ,'home.html', context)