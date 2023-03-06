from django.contrib import admin

from .models import VisitorUrl


class AdminVisitorUrl(admin.ModelAdmin):
    pass


admin.site.register(VisitorUrl, AdminVisitorUrl)
