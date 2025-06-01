from django import forms
from ..models import Profile



class ProfileCreateForm(forms.ModelForm):
   
    class Meta:
        model = Profile
        fields = [
            'fname',
            'lname',
            'email',
            'mobile',
            'contactperson',
            'mobileofcontactperson',
            ]
        
    fname = forms.CharField(widget=forms.TextInput(
                attrs={"placeholder": "Firstname"}), label='Firstname')
    lname = forms.CharField(widget=forms.TextInput(
                attrs={"placeholder": "Lastname"}), label='Lastname')
    email = forms.CharField(widget=forms.TextInput(
                attrs={"placeholder": "Email Address -- optional "}), required=False)
    mobile = forms.DecimalField(widget=forms.NumberInput(
                attrs={"placeholder": "Mobile Number"}), required=False, max_digits=11)
    contactperson = forms.CharField(widget=forms.TextInput(
                attrs={"placeholder": "Contact Person / Caretaker -- optional"}), required=False, label='Contact Person')
    mobileofcontactperson = forms.DecimalField(widget=forms.NumberInput(
                attrs={"placeholder": "Mobile of contact person / Caretaker -- optional"}), required=False, max_digits=11,label='Mobile of contact Person')
    

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'fname',
            'lname',
            'email',
            'mobile',
            'contactperson',
            'mobileofcontactperson',
            ]
    fname = forms.CharField(widget=forms.TextInput(
                attrs={"placeholder": "Firstname"}), label='Firstname')
    lname = forms.CharField(widget=forms.TextInput(
                attrs={"placeholder": "Lastname"}), label='Lastname')
    email = forms.CharField(widget=forms.TextInput(
                attrs={"placeholder": "Email Address -- optional "}), required=False)
    mobile = forms.DecimalField(widget=forms.NumberInput(
                attrs={"placeholder": "Mobile Number"}), required=False, max_digits=11)
    contactperson = forms.CharField(widget=forms.TextInput(
                attrs={"placeholder": "Contact Person / Caretaker -- optional"}), required=False)
    mobileofcontactperson = forms.DecimalField(widget=forms.NumberInput(
                attrs={"placeholder": "Mobile of contact person / Caretaker -- optional"}), required=False, max_digits=11)
