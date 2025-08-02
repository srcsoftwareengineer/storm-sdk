'''
Created on 15 de jul. de 2025

@author: masterdev
'''

import random
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from models import Raffle, WinnerNotification, Ticket
from forms import RaffleForm


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("core:dashboard")
    else:
        form = UserCreationForm()
    return render(request, "core/sign_up.html", {"form": form})

@login_required
def dashboard(request):
    return render(request, "core/dashboard.html")

@login_required
def draw_raffle(request, raffle_id):
    raffle = get_object_or_404(Raffle, id=raffle_id, created_by=request.user, status="published")
    tickets = Ticket.objects.filter(raffle=raffle, payment_confirmed=True)

    if tickets.exists():
        winner_ticket = random.choice(tickets)
        WinnerNotification.objects.create(raffle=raffle, winner=winner_ticket.buyer)
        raffle.status = "finished"
        raffle.save()
    return redirect('core:list_raffles')

@login_required
def create_raffle(request):
    if request.method == 'POST':
        form = RaffleForm(request.POST)
        if form.is_valid():
            raffle = form.save(commit=False)
            raffle.created_by = request.user
            raffle.save()
            return redirect('core:list_raffles')
    else:
        form = RaffleForm()
    return render(request, 'core/create_raffle.html', {'form': form})

@login_required
def publish_raffle(request, raffle_id):
    raffle = get_object_or_404(Raffle, id=raffle_id, created_by=request.user)
    if raffle.status == "draft":
        raffle.status = "published"
        raffle.save()
    return redirect('core:list_raffles')

@login_required
def list_raffles(request):
    raffles = Raffle.objects.filter(created_by=request.user)
    return render(request, 'core/list_raffles.html', {'raffles': raffles})
