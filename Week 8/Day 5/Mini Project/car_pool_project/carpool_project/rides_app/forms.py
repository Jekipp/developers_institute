from django import forms
from .models import Traveler, Trip

class TravelerForm(forms.ModelForm):

    class Meta:      
        model = Traveler
        fields = '__all__'

class TripForm(forms.ModelForm):

    class Meta:
        model = Trip
        exclude = ['driver', 'passengers']