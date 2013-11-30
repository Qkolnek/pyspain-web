# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url

from . import views

urlpatterns = patterns('',
    url(r"^$", views.Home.as_view(), name="home"),
    url(r"^article/(?P<slug>[\w\d\-]+)$", views.Article.as_view(), name="article"),
    url(r"^faq$", views.Faq.as_view(), name="faq-list"),
)
