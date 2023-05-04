from django.contrib import admin

from .models import Mensaje

# Register your models here.


class MensajeAdmin(admin.ModelAdmin):
    fields = ["usuario", "titulo", "contenido", "fecha"]
    list_display = ("id", "usuario", "titulo")


admin.site.register(Mensaje, MensajeAdmin)
