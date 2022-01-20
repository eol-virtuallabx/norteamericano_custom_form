from django.contrib import admin
from .models import NAExtraInfo

class NAExtraInfoAdmin(admin.ModelAdmin):
    raw_id_fields = ('user',)
    list_display = ('na_rut', 'user')
    search_fields = ['na_rut', 'user__username']
    ordering = ['-na_rut']

admin.site.register(NAExtraInfo, NAExtraInfoAdmin)
