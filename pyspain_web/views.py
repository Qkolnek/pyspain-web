# -*- coding: utf-8 -*-

from pyspain.views import GenericView, GenericTemplateView


class Home(GenericTemplateView):
    tmpl_name = "web/home.jinja"

