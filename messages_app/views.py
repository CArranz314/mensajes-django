from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from .models import Message
from .tables import MessageTable
from .forms import CreateAccount, CreateMessage

# Create your views here.


def list(request):
    """
    View for listing all messages
    """

    messages = Message.objects.all()
    table = MessageTable(messages)
    context = {"messages": table}
    return render(request, "messages_app/list.html", context)


def results(request):
    """
    View for listing messages whose content matches the search terms
    """
    search = request.GET.get("search")
    # por ahora usa el template de index, pero debería tener uno propio

    if len(search) == 0:
        messages = Message.objects.all()
        table = MessageTable(messages)
        context = {"messages": table}
        return render(request, "messages_app/list.html", context)
    else:
        messages = Message.objects.all().filter(
            Q(title__icontains=search) | Q(content__icontains=search)
        )
        table = MessageTable(messages)
        context = {"messages": table, "search": search, "total": len(messages)}
        return render(request, "messages_app/results.html", context)


@login_required
def new_message(request):
    """
    View for creating new messages
    """
    if request.method == "POST":
        form = CreateMessage(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.date = timezone.now()
            message.user = request.user
            message.save()

            return redirect("messages_app:list")
    else:
        form = CreateMessage()
    context = {"form": form}
    return render(request, "messages_app/new_message.html", context)


def message_detail(request, pk):
    """
    View for showing all the data of a single message
    """
    message = get_object_or_404(Message, pk=pk)
    context = {"message": message}
    return render(request, "messages_app/message_detail.html", context)


# realmente la parte de creacion de cuentas debería estar en su propia APP
def create_account(request):
    """
    Vista para crear un usuario
    """
    if request.method == "POST":
        form = CreateAccount(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()

            return redirect("messages_app:login")
    else:
        form = CreateAccount()
    return render(request, "messages_app/create_account.html", {"form": form})
