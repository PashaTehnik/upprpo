from django.contrib import admin

from .models import GameHtml5


class GameAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('id', "src", 'description', 'image', 'genre')
        }),
        ('Advanced options', {
            'classes': ('collapse',),
            'fields': (),
        }),
    )
    #fields = ('id', "src", "description", 'image')
    list_display = ('id', 'genre', 'description',  'src')


admin.site.register(GameHtml5, GameAdmin)
