from django.shortcuts import render
from websurat.models import Surat
from websurat.forms import FormSuratKeluar

def surat_masuk(request):

    surat = Surat.objects.all().order_by('-nomor_surat')

    konteks={
        'surat': surat,
    }

    return render(request, 'surat_masuk.html', konteks)