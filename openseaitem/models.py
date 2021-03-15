from django.db import models
from django.utils.translation import ugettext_lazy as _

from web.mixins.models import StatusModel


# Create your models here.
class OpenSeaItem(StatusModel):
	title = models.CharField(
		max_length=50,
		unique=True
	)
	meta = models.JSONField(
		null=False,
		blank=False,
		help_text=_('See all available Metadata <a href="https://docs.opensea.io/docs/metadata-standards">here</a>')
	)

	class Meta:
		verbose_name = _('Open Sea Item')
		verbose_name_plural = _('Open Sea Items')

	def __str__(self):
		return '{}'.format(self.title)
