from django.contrib import admin
from .models import TextItem, Participant, Response
from import_export.admin import ExportMixin
from import_export import resources


# Resource für Responses inkl. Teilnehmerdaten
class ResponseResource(resources.ModelResource):
    class Meta:
        model = Response
        fields = (
            "participant__id",
            "participant__name",
            "participant__experience",
            "participant__department",
            "text__id",
            "text__title",
            "text__origin",
            "classification",
            "confidence",
            "response_time",
            "index",
        )
        export_order = fields


class ResponseAdmin(ExportMixin, admin.ModelAdmin):
    resource_class = ResponseResource
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


@admin.register(Response)
class ResponseAdmin(ResponseAdmin):
    pass


class ResponseInline(admin.TabularInline):
    model = Response
    extra = 0
    readonly_fields = ("text", "classification", "confidence", "response_time", "index")
    can_delete = False


@admin.register(Participant)
class ParticipantAdmin(ExportMixin, admin.ModelAdmin):
    list_display = ("name", "experience", "department", "created_at")
    search_fields = ("name", "department")
    list_filter = ("department",)
    inlines = [ResponseInline]


@admin.register(TextItem)
class TextItemAdmin(admin.ModelAdmin):
    list_display = ("title", "origin")
    list_filter = ("origin",)
    search_fields = ("title", "body")
