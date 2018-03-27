# -*- coding: utf-8 -*-
from django.conf.urls import url

from . import views

urlpatterns=[

        url(r'^index/$',views.index),
        url(r'^article/(?P<article_id>[0-9]+)$',views.article_page,name="article_page"),
       
        url(r'^get_content/',views.get_content),
        url(r'^uploadEditor/',views.uploadEditor),
        url(r'^uploadPaste',views.uploadPaste),
        url(r'^work',views.work),
        url(r'^project_view/(?P<project_id>[0-9]+)$',views.project_view,name="project_view"),
        url(r'^project_del/(?P<project_id>[0-9]+)$',views.project_del,name="project_del"),
        url(r'^project_add/$',views.project_add,name="project_add"),
        url(r'^bug_view/(?P<bug_id>[0-9]+)$',views.bug_view,name="bug_view"),
        url(r'^bug_del/(?P<bug_id>[0-9]+)$',views.bug_del,name="bug_del"),
        url(r'^bug_add/(?P<project_id>[0-9]+)$',views.bug_add,name="bug_add"),
        url(r'^project_word/(?P<project_id>[0-9]+)$',views.project_word,name="project_word"),
        url(r'^select/$',views.select),
        
        
        
        
        
        
        
        
        ]