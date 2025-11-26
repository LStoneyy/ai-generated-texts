from django.contrib import admin
from .models import TextItem, Participant, Response
from import_export.admin import ExportMixin



@admin.register(Participant)
class ParticipantAdmin(ExportMixin, admin.ModelAdmin):
    list_display = ("name", "experience", "department", "created_at")
    search_fields = ("name", "department")
    list_filter = ("department",)
    inlines = [ResponseInline]


@admin.register(Response)
class ResponseAdmin(ExportMixin, admin.ModelAdmin):
    list_display = (
        "participant",
        "text",
        "classification",
        "confidence",
        "response_time",
        "index",
    )
    list_filter = ("classification", "text")
    search_fields = ("participant__name", "text__title")


@admin.register(TextItem)
class TextItemAdmin(admin.ModelAdmin):
    list_display = ("title", "origin")
    list_filter = ("origin",)
    search_fields = ("title", "body")
