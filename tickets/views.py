# from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Ticket, TicketReply
from .forms import TicketForm, ReplyForm
from django.contrib import messages

@login_required
def create_ticket(request):
    if request.method == 'POST':
        form = TicketForm(request.POST, request.FILES)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.customer = request.user
            ticket.save()
            messages.success(request, "Ticket created.")
            return redirect('tickets:ticket_detail', pk=ticket.pk)
    else:
        form = TicketForm()
    return render(request, 'tickets/create_ticket.html', {'form': form})

@login_required
def ticket_detail(request, pk):
    ticket = get_object_or_404(Ticket, pk=pk)
    replies = ticket.replies.all().order_by('created_at')
    if request.method == 'POST':
        form = ReplyForm(request.POST, request.FILES)
        if form.is_valid():
            reply = form.save(commit=False)
            reply.ticket = ticket
            reply.sender = request.user
            reply.save()
            # optionally create ActivityLog
            messages.success(request, "Reply added.")
            return redirect('tickets:ticket_detail', pk=pk)
    else:
        form = ReplyForm()
    return render(request, 'tickets/ticket_detail.html', {'ticket': ticket, 'replies': replies, 'form': form})


from rest_framework import serializers
from .models import Ticket, TicketReply

class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = '__all__'

class TicketReplySerializer(serializers.ModelSerializer):
    class Meta:
        model = TicketReply
        fields = '__all__'
from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Ticketing System Home Page")
