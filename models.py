from django.db import models
from mezzanine.pages.models import Page, Link


# Create your models here.
class Section(Page):
    icon = models.CharField(max_length=30, null=True, blank=True)

class LinkIcon(Link):
    icon = models.CharField(max_length=30, null=True, blank=True)