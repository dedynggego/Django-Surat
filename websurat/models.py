from django.db import models

# Create your models here.
class Surat(models.Model):
    tgl_surat = models.CharField(max_length=50, null=True)
    nomor_surat = models.CharField(max_length=50, null=True)
    jenis_surat = models.CharField(max_length=50, null=True)
    tujuan = models.CharField(max_length=50, null=True)
    perihal = models.CharField(max_length=50, null=True)
    mengetahui = models.CharField(max_length=50, null=True)
    arsip = models.CharField(max_length=50, null=True)
    ket = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.tgl_surat

    



