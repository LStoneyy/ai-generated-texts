from django import forms
from .models import Participant


class ParticipantForm(forms.ModelForm):
    class Meta:
        model = Participant
        fields = ["name", "experience", "department"]
        widgets = {
            "name": forms.TextInput(attrs={"required": True}),
            "experience": forms.NumberInput(attrs={"required": True, "min": 0}),
            "department": forms.TextInput(attrs={"required": True}),
        }


class ResponseForm(forms.Form):
    CLASSIFICATION_CHOICES = [
        ("human", "Human-written"),
        ("ai", "AI-generated"),
    ]
    classification = forms.ChoiceField(
        choices=CLASSIFICATION_CHOICES, widget=forms.RadioSelect, required=True
    )
    confidence = forms.ChoiceField(
        choices=[(i, str(i)) for i in range(1, 6)], widget=forms.Select, required=True
    )
    response_time = forms.IntegerField(widget=forms.HiddenInput())
