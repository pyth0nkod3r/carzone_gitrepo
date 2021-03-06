from django.contrib import admin
from django.utils.html import format_html

from .models import Team

# Register your models here.


class AdminTeam(admin.ModelAdmin):
    def thumbnail(self, obj):
        return format_html(
            '<img src="{}" width="40" height="40" style="border-radius: 50px; "/>'.format(obj.photos.url)
        )
    thumbnail.short_description = 'Photo'
    list_display = ('id', 'thumbnail', 'first_name', 'last_name', 'position', 'created_date',)
    list_display_links = ('id', 'first_name', 'thumbnail',)
    list_filter = ('position',)
    search_fields = ('first_name', 'last_name', 'position',)



admin.site.register(Team, AdminTeam)

