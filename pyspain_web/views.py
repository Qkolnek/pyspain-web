# -*- coding: utf-8 -*-

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import get_model
from django.utils.text import Truncator
from django.shortcuts import get_object_or_404

from markdown import markdown

from pyspain.views import GenericView, GenericTemplateView


class MarkupMixin(object):
    def markup(self, text, truncate=True):
        if truncate:
            t = Truncator(text)
            text = t.chars(1000)

        return markdown(text, safe_mode=False)


class Home(MarkupMixin, GenericTemplateView):
    tmpl_name = "web/home.jinja"

    def get_context_data(self):
        ctx = super().get_context_data()

        article_cls = get_model("content", "Article")

        queryset = article_cls.objects.all().order_by("-created_at")
        paginator = Paginator(queryset, 5)

        page = self.request.GET.get('page')
        try:
            articles = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            articles = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            articles = paginator.page(paginator.num_pages)

        ctx["paginator"] = paginator
        ctx["articles"] = articles

        return ctx


class Article(MarkupMixin, GenericTemplateView):
    tmpl_name = "web/article.jinja"

    def get_context_data(self):
        ctx = super().get_context_data()
        article_cls = get_model("content", "Article")
        article = get_object_or_404(article_cls, slug=self.kwargs["slug"])

        ctx["article"] = article
        return ctx


class Faq(MarkupMixin, GenericTemplateView):
    def get_tmpl_name(self):
        return "web/faq-list.jinja"

    def get_context_data(self):
        ctx = super().get_context_data()
        faq_entry_cls = get_model("content", "FaqEntry")
        ctx["entries"] = faq_entry_cls.objects.all().order_by("question")
        return ctx
