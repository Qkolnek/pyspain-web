# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _


class AbstactContent(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    modified_at = models.DateTimeField(auto_now=True, blank=True)

    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=500)
    content = models.TextField()

    created_by = models.ForeignKey("users.User", null=True, blank=True, related_name="+",
                                   default=None, verbose_name=_("Creado por"))

    class Meta:
        abstract = True


class Page(AbstactContent):
    pass


class Article(AbstactContent):
    pass


class FaqEntry(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    modified_at = models.DateTimeField(auto_now=True, blank=True)

    question = models.TextField()
    response = models.TextField()

    created_by = models.ForeignKey("users.User", null=True, blank=True, related_name="+",
                                   default=None, verbose_name=_("Creado por"))
