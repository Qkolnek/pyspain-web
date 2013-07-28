# -*- coding: utf-8 -*-

from django.contrib import admin
from . import models


class AccountingEntryRegisterInline(admin.TabularInline):
    model = models.AccountingEntryRegister
    extra = 0
    readonly_fields = ('id',)
    fields = ('id', 'account', 'invoice')


class InvoiceAdmin(admin.ModelAdmin):
    actions_on_top = True


class AccountingEntryRegisterAdmin(admin.ModelAdmin):
    actions_on_top = True


class AccountingEntryAdmin(admin.ModelAdmin):
    actions_on_top = True
    inlines = [AccountingEntryRegisterInline]
    readonly_fields = ('id',)
    fields = ('id', 'date',)


admin.site.register(models.Invoice, InvoiceAdmin)
admin.site.register(models.AccountingEntry, AccountingEntryAdmin)
admin.site.register(models.AccountingEntryRegister, AccountingEntryRegisterAdmin)
