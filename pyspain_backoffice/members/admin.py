# -*- coding: utf-8 -*-

from django.contrib import admin
from . import models


class PaymentInline(admin.TabularInline):
    model = models.MemberPayment
    extra = 0
    readonly_fields = ('id',)
    fields = ('id', 'quantity', 'payment_date',)


class MemberAdmin(admin.ModelAdmin):
    actions_on_top = True

    list_display = ('full_name', 'email', 'phone',
                    'joined_at', 'internal_account_number',)

    list_display_links = list_display
    search_fields = ["full_name", "email", "phone"]
    date_hierarchy = 'joined_at'

    inlines = [PaymentInline]

    fieldsets = (
        (None, {
            'fields': (
                ('full_name', 'identity_number'),
                ('email', 'phone'),
                ('address',),
            )
        }),
        ("Fechas", {
            'fields': (('created_at', 'joined_at'),),
        }),
        ("Social", {
            'fields': ('twitter_username',
                       'github_username',
                       'webpage_url'),
        }),
        ("Metadatos", {
            'classes': ('collapse',),
            'fields': ('user', 'board_of_trustees',
                       'internal_account_number',),
        }),
    )


class MemberPaymentAdmin(admin.ModelAdmin):
    actions_on_top = True

    list_display = ("member", "payment_date", "quantity")
    list_display_links = list_display
    date_hierarchy = 'payment_date'


admin.site.register(models.Member, MemberAdmin)
admin.site.register(models.MemberPayment, MemberPaymentAdmin)
