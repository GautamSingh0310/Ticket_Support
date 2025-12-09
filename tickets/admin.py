# from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Department, Ticket, TicketReply, InternalNote, ActivityLog

admin.site.register(Department)
admin.site.register(Ticket)
admin.site.register(TicketReply)
admin.site.register(InternalNote)
admin.site.register(ActivityLog)
