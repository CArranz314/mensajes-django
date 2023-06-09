from .models import Message
import django_tables2 as tables
from django_tables2.utils import A
from django.utils.translation import gettext_lazy as _


class MessageTable(tables.Table):
    """
    Custom table for displaying messages
    """

    # additional field with links to the detailed message page
    detail = tables.LinkColumn(
        "messages_app:message_detail",
        verbose_name=_("detail"),
        text=_("MORE"),
        args=[A("pk")],
    )

    class Meta:
        # class the table is modeled after
        model = Message
        # fields we don´t want on the table(WARNING: it´s supposed to be a tuple, don´t delete the comma)
        exclude = ("content",)
        template_name = "messages_app/a.html"
