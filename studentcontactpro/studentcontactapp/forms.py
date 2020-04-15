from django import forms
from multiselectfield import MultiSelectFormField

class StudentForm(forms.Form):
    sname = forms.CharField(
        label= "Enter Student Name",
        widget=forms.TextInput(
            attrs={
                'placholder': 'Student Name',
                'class':'form-control'
            }
        )
    )
    fname= forms.CharField(
        label="Enter Father Name",
        widget=forms.TextInput(
            attrs={
                'placholder': 'Father Name',
                'class': 'form-control'
            }
        )
    )
    sloc = forms.CharField(
        label="Enter Student Location",
        widget=forms.TextInput(
            attrs={
                'placholder': 'Student Location',
                'class': 'form-control'
            }
        )
    )
    scontact = forms.IntegerField(
        label="Enter Student Contact",
        widget=forms.NumberInput(
            attrs={
                'placholder': 'Student Contact',
                'class': 'form-control'
            }
        )
    )
    gender_choice=(('M', 'Male'), ('F','Female'))
    sgender=forms.ChoiceField(
        widget=forms.RadioSelect(),choices=gender_choice
    )
