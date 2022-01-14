from django.contrib import admin

# Register your models here.
from apps.driving.models import Chapter, Ticket


@admin.register(Chapter)
class ChapterAdmin(admin.ModelAdmin):
    list_display = ['id', 'text']

@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ['id', 'chapter', 'question', 'picture', 'answer', 'explanation']
