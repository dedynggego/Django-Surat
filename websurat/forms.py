from django.db.models import fields
from django.forms import ModelForm
from websurat.models import Surat

class FormSuratKeluar(ModelForm):
    class Meta:
        model = Surat
        fields = '__all__'