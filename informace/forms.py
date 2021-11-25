from django import forms

from .models import Zvire

# class ZvireForm(forms.Form):
#     jmeno = forms.CharField(label="Jméno zvířete", max_length=20,
#         error_messages = {
#             "required": "Tohle políčko musíš vyplnit!!",
#             "max_length": "Fakt má tvoje zvíře takhle nesmyslně dlouhý jméno??"
#         })
#     vaha = forms.IntegerField()
#     barva = forms.CharField()
#     zije = forms.BooleanField(required=False)

class ZvireForm(forms.ModelForm):
    class Meta:
        model = Zvire
        fields = ["jmeno"]
        labels = {
            "jmeno": "Jmeno zvířete",
            "vaha": "Kolik vážíš?"
        }
        error_messages = {
            "jmeno": {
                 "required": "Jméno musíš vyplnit!!",
                 "max_length": "Fakt má tvoje zvíře takhle nesmyslně dlouhý jméno??"
            },
            "vaha": {
                "required": "Váhu musíš vyplnit!!",
            }
        }

    