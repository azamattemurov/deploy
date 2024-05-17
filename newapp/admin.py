from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Comment)


@admin.register(News)
class Bookadmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'year')
    list_filter = ['title', 'year']
    readonly_fields = ['image_tag']


