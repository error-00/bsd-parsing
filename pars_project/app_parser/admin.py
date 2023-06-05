from django.contrib import admin

from .models import *


# admin 1111

@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = ('name', 'link', 'status')


@admin.register(Info)
class InfoAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'type', 'domesticity', 'registered_agent', 'date_formed', 'duration', 'renewal_month', 'report_due',
        'chapter', 'home_state', 'status', 'link',)


@admin.register(Keys_w)
class KeysAdmin(admin.ModelAdmin):
    list_display = ('name', 'status',)
