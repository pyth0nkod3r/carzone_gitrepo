from django.contrib import admin
from django.utils.html import format_html

from .models import Car

# Register your models here.


class CarAdmin(admin.ModelAdmin):

    def thumbnail(self, obj):
        return format_html(
            '<img src="{}" width="50" height="40" style="border-radius:50px;" />'.format(obj.main_photo.url)
        )
    list_display = (
        'id', 'thumbnail', 'car_name', 'state', 'color', 'fuel_type', 'is_featured'
    )
    thumbnail.short_description = 'Car Image'
    list_display_links = ('id', 'thumbnail', 'car_name',)
    list_filter = ('color', )
    search_fields = ('name', 'city', 'state')
    list_editable = ('is_featured',)


admin.site.register(Car, CarAdmin)

