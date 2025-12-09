from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Ticket, TicketReply
from django.core.mail import send_mail

@receiver(post_save, sender=Ticket)
def notify_ticket_created(sender, instance, created, **kwargs):
    if created:
        # send email to admins/agents
        send_mail(
            f'New ticket {instance.ticket_id}',
            instance.description,
            'no-reply@support.com',
            ['agent@example.com'],
            fail_silently=True
        )

@receiver(post_save, sender=TicketReply)
def notify_on_reply(sender, instance, created, **kwargs):
    if created:
        # send email to ticket.customer or agent
        pass
