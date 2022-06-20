from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    pass


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    pass


@admin.register(TextMessage)
class TextMessageAdmin(admin.ModelAdmin):
    pass
