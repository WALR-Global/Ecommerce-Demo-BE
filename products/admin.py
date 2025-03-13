from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from products.models import Type


# Register your models here.
@admin.register(Type)
class Type(ImportExportModelAdmin):
    pass
