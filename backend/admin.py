from django.contrib import admin
from .models import ZipCode, DoctorData, OldData
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Register your models here.
class Zip_CodeResource(resources.ModelResource):
    class Meta:
        model = ZipCode


class Zip_CodeAdmin(ImportExportModelAdmin):
    resource_class = Zip_CodeResource


admin.site.register(ZipCode, Zip_CodeAdmin)


class OldResource(resources.ModelResource):
    class Meta:
        model = OldData


class OldAdmin(ImportExportModelAdmin):
    resource_class = OldResource


admin.site.register(OldData, OldAdmin)


class DoctorResource(resources.ModelResource):
    class Meta:
        model = DoctorData
        exclude = ('relation_manager', )


class DoctorAdmin(ImportExportModelAdmin):
    resource_class = DoctorResource


admin.site.register(DoctorData, DoctorAdmin)

