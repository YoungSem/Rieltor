from django import forms
from .models import Application, Flat

class ApplicationForm(forms.ModelForm):
    flat = forms.ModelChoiceField(
        queryset=Flat.objects.all(),
        required=False,
        empty_label="Выберите квартиру (необязательно)",
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Application
        fields = ['person_name', 'email', 'tel', 'flat']
        widgets = {
            'person_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ваше имя'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'tel': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Телефон'}),
        } 