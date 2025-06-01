from django import forms
from .models import House
from profiles.models import Profile

class HouseCreateForm(forms.ModelForm):

    class Meta:
        model = House
        fields = [
            'block_number',
            'lot_number',
            'owner',
        ]
            
       
    block_number = forms.IntegerField(
        label = 'Block Number:',
        required=False,
        widget=forms.NumberInput(attrs={'placeholder': 'Block Number'})
    )

    lot_number = forms.IntegerField(
        label= 'Lot Number:',
        widget=forms.NumberInput(attrs={'placeholder': 'Lot Number'})
    )

    owner = forms.ModelChoiceField(
        queryset = Profile.objects.all(),
        empty_label='---------List of Owner-----------',
        to_field_name='id',
        required=True,
        widget=forms.Select(attrs={'class': ''})
    )
    
    




    
