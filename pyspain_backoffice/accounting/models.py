# -*- coding: utf-8 -*-

from django.utils.translation import ugettext_lazy as _
from django.utils.translation import ugettext
from django.db import models
from django.utils import timezone


class Invoice(models.Model):
    identifier = models.CharField(max_length=255,
                                  verbose_name=_("Numero de factura"))

    attachment = models.FileField(upload_to="invoices/%d/%Y",
                                  verbose_name=_("Factura en pdf"))

    created_at = models.DateTimeField(
                    verbose_name=_("Fecha de creación"),
                    default=timezone.now)

    class Meta:
        ordering = ["identifier"]
        verbose_name = _("Factura")
        verbose_name_plural = _("Facturas")


class AccountingEntry(models.Model):
    date = models.DateField(default=lambda: timezone.now().date(),
                            verbose_name=_("Fecha"))

    class Meta:
        ordering = ["date"]
        verbose_name = _("Asiento")
        verbose_name_plural = _("Asientos")

    def __str__(self):
        return ugettext("Asiento {0}").format(self.id)


class AccountingEntryRegister(models.Model):
    accountin_entry = models.ForeignKey("AccountingEntry",
                                        related_name="registers",
                                        verbose_name=_("Asiento"))

    account = models.CharField(max_length=100,
                               verbose_name=_("Numero de cuenta"))

    invoice = models.ForeignKey("Invoice", related_name="registers",
                                verbose_name=_("Factura"),
                                null=True, blank=True)

    created_at = models.DateTimeField(
                    verbose_name=_("Fecha de creación"),
                    default=timezone.now)

    class Meta:
        ordering = ["created_at"]
        verbose_name = _("Registro")
        verbose_name_plural = _("Registros")
