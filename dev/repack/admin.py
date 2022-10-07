from django.contrib import admin
from repack.models import Item, Contact
from django.utils.safestring import mark_safe

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'description', 'get_cover_image')

    def get_cover_image(self, obj):
        if obj.image:
            return mark_safe('<img src="{}" style="width:100px;height:75px;" />'.format(obj.image.url))
        else:
            return mark_safe("<i style='color:red;'>no image</i>")
    get_cover_image.short_description = 'Cover Image'

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'message')