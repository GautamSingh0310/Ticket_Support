from django.urls import path
from . import views

app_name = "tickets"

urlpatterns = [
    path("create/", views.create_ticket, name="create_ticket"),
    path("<int:pk>/", views.ticket_detail, name="ticket_detail"),
    path("", views.home, name="home"),
]


