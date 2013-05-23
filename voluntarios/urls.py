#encoding: utf-8

from django.conf.urls import patterns, include, url

urlpatterns = patterns('voluntarios.views',
    url(r'^$', 'index', name='voluntarios'),
    url(r'^gti/$', 'gti', name='voluntarios_gti'),

)