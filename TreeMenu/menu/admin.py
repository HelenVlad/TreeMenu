from django.contrib import admin
from .models import MenuItem

class ChildMenuItemInline(admin.TabularInline):
    """
    Встраиваемая форма для отображения дочерних пунктов меню, связанных с родительским пунктом меню.
    """
    model = MenuItem
    fk_name = 'higher_level'
    fields = ('name_item', 'id', 'named_url', 'url')
    readonly_fields = ('id', 'name_item', 'named_url', 'url')
    extra = 0

class MenuItemAdmin(admin.ModelAdmin):
    """
    Конфигурация админ-панели для пунктов меню.

    Определяет, как пункты меню отображаются и управляются в админ-панели.
    """
    list_display = ('id', 'name_item', 'higher_level_id', 'named_url', 'url')
    list_display_links = ('name_item',)
    list_filter = ('id', 'name_item', 'higher_level_id')
    inlines = (ChildMenuItemInline,)

admin.site.register(MenuItem, MenuItemAdmin)
