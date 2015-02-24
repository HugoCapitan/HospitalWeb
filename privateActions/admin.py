from django.contrib import admin

from .models import Diagnostic, Message

admin.site.register(Diagnostic)
admin.site.register(Message)
