# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _


class StatusModel(models.Model):
    STATUS_CODES = (
        (0, _('disable')),
        (1, _('enable')),
    )
    status = models.IntegerField(
        choices=STATUS_CODES,
        default=1,
        verbose_name=_('status'),
        null=True
    )

    class Meta:
        abstract = True