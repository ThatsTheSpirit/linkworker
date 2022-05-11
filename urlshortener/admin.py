from django.contrib import admin
from .models import Link


# Register your models here.


class LinkAdmin(admin.ModelAdmin):
    # list_display = ('id', 'short_url', 'creation_date', 'expiration_date')
    # list_display_links = ('id', 'short_url')
    # search_fields = ('full_url', 'creation_date', 'expiration_date')
    list_display = ('short_url', 'creation_date', 'expiration_date')
    list_display_links = ('short_url',)
    search_fields = ('full_url', 'creation_date', 'expiration_date')


admin.site.register(Link, LinkAdmin)
