# -*- coding: utf-8 -*-

from django.contrib.syndication.views import Feed
from django.core.urlresolvers import reverse

from .content.models import Article
from . import utils


class ArticlesFeed(Feed):
    title = "Ultimas noticias de Python España"
    description = ""
    link = "/"

    def items(self):
        return Article.objects.order_by("-created_at")[:20]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return utils.markup(item.content)

    def item_link(self, item):
        return reverse("article", args=[item.slug])
