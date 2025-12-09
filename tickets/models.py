# from django.db import models

# Create your models here.
from django.conf import settings
from django.db import models
from django.utils import timezone
import uuid

User = settings.AUTH_USER_MODEL

class Department(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self): return self.name

class Ticket(models.Model):
    STATUS_CHOICES = [
        ('open','Open'),
        ('in_progress','In Progress'),
        ('resolved','Resolved'),
        ('closed','Closed'),
    ]
    PRIORITY_CHOICES = [('low','Low'),('medium','Medium'),('high','High'),('urgent','Urgent')]
    
    attachment = models.FileField(upload_to='ticket_attachments/', blank=True, null=True)
    ticket_id = models.CharField(max_length=20, unique=True, editable=False)
    title = models.CharField(max_length=255)
    description = models.TextField()
    customer = models.ForeignKey(User, related_name='tickets', on_delete=models.CASCADE)
    agent = models.ForeignKey(User, related_name='assigned_tickets', null=True, blank=True, on_delete=models.SET_NULL)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='medium')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='open')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.ticket_id:
            self.ticket_id = 'TKT-' + uuid.uuid4().hex[:8].upper()
        super().save(*args, **kwargs)

    def __str__(self): return f'{self.ticket_id} - {self.title}'

class TicketReply(models.Model):
    ticket = models.ForeignKey(Ticket, related_name='replies', on_delete=models.CASCADE)
    sender = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    message = models.TextField()
    attachment = models.FileField(upload_to='ticket_attachments/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

class InternalNote(models.Model):
    ticket = models.ForeignKey(Ticket, related_name='internal_notes', on_delete=models.CASCADE)
    agent = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    note = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class ActivityLog(models.Model):
    ticket = models.ForeignKey(Ticket, related_name='activities', on_delete=models.CASCADE)
    action = models.CharField(max_length=255)
    done_by = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    timestamp = models.DateTimeField(default=timezone.now)
