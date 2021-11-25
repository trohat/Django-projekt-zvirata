from django import forms

class ZvireForm(forms.Form):
    jmeno = forms.CharField(label="Jméno zvířete", max_length=20,
        error_messages = {
            "required": "Tohle políčko musíš vyplnit!!",
            "max_length": "Fakt má tvoje zvíře takhle nesmyslně dlouhý jméno??"
        })
    vaha = forms.IntegerField()
    barva = forms.CharField()
    zije = forms.BooleanField(required=False)
