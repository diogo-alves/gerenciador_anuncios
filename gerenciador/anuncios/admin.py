from django.contrib import admin

from .models import Anuncio


class AnuncioAdmin(admin.ModelAdmin):
    pass


admin.site.register(Anuncio, AnuncioAdmin)
