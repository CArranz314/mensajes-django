from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required

from .models import Mensaje
from .tables import MensajeTable
from .forms import CrearCuenta, CrearMensaje

# Create your views here.


def listar(request):
    """
    Vista que devuelve una tabla con los mensajes
    """
    mensajes = Mensaje.objects.all()
    # context = {"mensajes": mensajes}
    tabla = MensajeTable(mensajes)
    context = {"mensajes": tabla}
    return render(request, "mensajes/listar.html", context)


@login_required
def nuevo_mensaje(request):
    """
    Vista que permite escribir un nuevo mensaje
    """
    if request.method == "POST":
        form = CrearMensaje(request.POST)
        if form.is_valid():
            mensaje = form.save(commit=False)
            mensaje.fecha = timezone.now()
            mensaje.usuario = request.user
            mensaje.save()

            return redirect("mensajes:listar")
    else:
        form = CrearMensaje()
    context = {"form": form}
    return render(request, "mensajes/nuevo_mensaje.html", context)


def ver_mensaje(request, pk):
    """
    Vista que permite ver el contenido de un mensaje individual
    """
    mensaje = get_object_or_404(Mensaje, pk=pk)
    context = {"mensaje": mensaje}
    return render(request, "mensajes/ver_mensaje.html", context)


# realmente la parte de creacion de cuentas debería estar en su propia APP
def crear_cuenta(request):
    """
    Vista para crear un usuario
    """
    if request.method == "POST":
        form = CrearCuenta(request.POST)
        if form.is_valid():
            usuario = form.save(commit=False)
            usuario.save()

            return redirect("mensajes:registro")
    else:
        form = CrearCuenta()
    return render(request, "mensajes/crear_cuenta.html", {"form": form})
