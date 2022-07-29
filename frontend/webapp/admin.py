from django.db import models
from django.contrib import admin
from django_monaco_editor.widgets import AdminMonacoEditorWidget
from webapp.models import AppModel

# Register your models here.

@admin.register(AppModel)
class AppModelAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': AdminMonacoEditorWidget}
    }