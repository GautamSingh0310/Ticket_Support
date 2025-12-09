from django import forms
from .models import Ticket, TicketReply

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['title','description','department','priority','attachment']  # if you add attachment to Ticket

class ReplyForm(forms.ModelForm):
    class Meta:
        model = TicketReply
        fields = ['message','attachment']
