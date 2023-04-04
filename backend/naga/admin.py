from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import NagaName, NagaData

class NagaAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'date')

class NagaResource(admin.ModelAdmin):
    list_display = ('title', 'rest')

admin.site.register(NagaData,NagaAdmin)
admin.site.register(NagaName,NagaResource)

