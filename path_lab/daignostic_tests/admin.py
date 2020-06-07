from django.contrib import admin

from .models import AntiBodies, ReferringDoctor, Patient, Panel

admin.site.site_header = 'Navani Pathology Lab'

@admin.register(AntiBodies)
class AdminAntiBodies(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Panel)
class AdminPanel(admin.ModelAdmin):
    list_display = ('name','antibody_names')

@admin.register(ReferringDoctor)
class AdminReferringDoctor(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone_number')

@admin.register(Patient)
class AdminPatient(admin.ModelAdmin):
    list_display = ('name', 'sex', 'dob', 'referring_doctor', 'diagnosis', 'state', 'panel_names', 'created', 'updated')
    list_filter = ('state', 'created', 'updated')