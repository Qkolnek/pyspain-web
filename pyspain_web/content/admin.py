# -*- coding: utf-8 -*-

from django.contrib import admin

from . import models


class ArticleAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ("title", "slug", "created_at", "modified_at", "created_by",)
    list_display_links = list_display


class PageAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ("title", "slug", "created_at", "modified_at", "created_by",)
    list_display_links = list_display


class FaqEntryAdmin(admin.ModelAdmin):
    list_display = ("question", "created_at", "modified_at", "created_by",)
    list_display_links = list_display


admin.site.register(models.Article, ArticleAdmin)
admin.site.register(models.Page, PageAdmin)
admin.site.register(models.FaqEntry, FaqEntryAdmin)
