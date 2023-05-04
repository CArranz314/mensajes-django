from .models import Mensaje
import django_tables2 as tables
from django_tables2.utils import A


class MensajeTable(tables.Table):
    """
    Tabla personalizada usando django_tables2
    """

    # campo adicional que te lleva a la pagina de detalles
    ver = tables.LinkColumn("mensajes:ver_mensaje", text="VER", args=[A("pk")])

    class Meta:
        # modelo sobre el que trabaja la tabla
        model = Mensaje
        # campos que no queremos(TIENE QUE SER UNA TUPLA, la coma al final es necesaria)
        exclude = ("contenido",)
        template_name = "django_tables2/semantic.html"
