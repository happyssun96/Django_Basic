from django.contrib import admin
from .models import Ouruser

class OuruserAdmin(admin.ModelAdmin):
    list_display = ('username', 'registered_dttm')

admin.site.register(Ouruser, OuruserAdmin)


