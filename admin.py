from django.contrib import admin
from mezzanine.pages.admin import PageAdmin
from .models import Section

admin.site.register(Section, PageAdmin)