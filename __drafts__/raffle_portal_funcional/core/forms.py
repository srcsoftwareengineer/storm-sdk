'''
Created on 15 de jul. de 2025

@author: Sandro Regis Cardoso
'''

from django import forms
from models import Raffle

class RaffleForm(forms.ModelForm):
    class Meta:
        model = Raffle
        fields = ['title', 'description', 'draw_date', 'ticket_price']
