from django.contrib import admin

from .models import Message

# Register your models here.


class MessageAdmin(admin.ModelAdmin):
    fields = ["user", "title", "content", "date"]
    list_display = ("id", "user", "title")


admin.site.register(Message, MessageAdmin)
