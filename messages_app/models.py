from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


# Create your models here.
class Message(models.Model):
    """
    Model class for Messages
    """

    user = models.ForeignKey(
        User, related_name="messages", on_delete=models.CASCADE, verbose_name=_("user")
    )
    title = models.CharField(_("title"), max_length=200, blank=True)
    content = models.TextField(verbose_name=_("content"))
    date = models.DateTimeField(verbose_name=_("date"))

    class Meta:
        ordering = ["-date"]
        verbose_name = _("message")
        verbose_name_plural = _("messages")

    def __str__(self):
        return self.title + " " + self.user.username
