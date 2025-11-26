from django.contrib import admin
from .models import TextItem


@admin.register(TextItem)
class TextItemAdmin(admin.ModelAdmin):
    list_display = ("title", "origin")
    list_filter = ("origin",)
    search_fields = ("title", "body")
