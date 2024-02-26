# from django.contrib import admin
# from .models import Municipality,AdministrativePost,Village,Aldeia,AcademicLevel,Religion,Profession

# # Register your models here.
# admin.site.register(Municipality)
# admin.site.register(AdministrativePost)
# admin.site.register(Village)
# admin.site.register(Aldeia)
from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import *
from import_export import resources
# Register your models here.
# class MunicipalityResource(resources.ModelResource):
#     class Meta:
#         model = Municipality
# class MunicipalityAdmin(ImportExportModelAdmin):
#     resource_class = MunicipalityResource
# admin.site.register(Municipality, MunicipalityAdmin)



# class AdministrativePostResource(resources.ModelResource):
#     class Meta:
#         model = AdministrativePost
# class AdministrativePostAdmin(ImportExportModelAdmin):
#     resource_class = AdministrativePostResource
# admin.site.register(AdministrativePost, AdministrativePostAdmin)



# class VillageResource(resources.ModelResource):
#     class Meta:
#         model = Village
# class VillageAdmin(ImportExportModelAdmin):
#     resource_class = VillageResource
# admin.site.register(Village, VillageAdmin)

# class AldeiaResource(resources.ModelResource):
#     class Meta:
#         model = Aldeia
# class AldeiaAdmin(ImportExportModelAdmin):
#     resource_class = AldeiaResource
# admin.site.register(Aldeia, AldeiaAdmin)

# class AcademicLevelResource(resources.ModelResource):
#     class Meta:
#         model = AcademicLevel
# class AcademicLevelAdmin(ImportExportModelAdmin):
#     resource_class = AcademicLevelResource
# admin.site.register(AcademicLevel, AcademicLevelAdmin)

# class ReligionResource(resources.ModelResource):
#     class Meta:
#         model = Religion
# class ReligionAdmin(ImportExportModelAdmin):
#     resource_class = ReligionResource
# admin.site.register(Religion, ReligionAdmin)
# admin.site.register(AcademicLevel)
# admin.site.register(Religion)
# admin.site.register(Profession)

