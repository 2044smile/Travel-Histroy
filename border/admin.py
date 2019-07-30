from django.contrib import admin
from .models import Border

class BorderAdmin(admin.ModelAdmin):
    list_display = ['id','title','created']
    list_filter = ['created', 'updated', 'author']
    search_fields = ['text', 'created']
    ordering = ['-updated', '-created']


admin.site.register(Border, BorderAdmin)