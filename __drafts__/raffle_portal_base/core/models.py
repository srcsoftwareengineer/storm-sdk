from django.db import models
from django.contrib.auth.models import User

class Raffle(models.Model):
    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('published', 'Published'),
        ('finished', 'Finished'),
    ]
    title = models.CharField(max_length=200)
    description = models.TextField()
    draw_date = models.DateField()
    ticket_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

class Ticket(models.Model):
    raffle = models.ForeignKey(Raffle, on_delete=models.CASCADE)
    buyer = models.ForeignKey(User, on_delete=models.CASCADE)
    number = models.PositiveIntegerField()
    payment_confirmed = models.BooleanField(default=False)

class WinnerNotification(models.Model):
    raffle = models.OneToOneField(Raffle, on_delete=models.CASCADE)
    winner = models.ForeignKey(User, on_delete=models.CASCADE)
    notified_at = models.DateTimeField(auto_now_add=True)
