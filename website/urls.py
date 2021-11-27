from django.contrib import admin
from django.urls import path
from websurat.views import surat_masuk


urlpatterns = [
    path('admin/', admin.site.urls),
    path('surat_masuk/', surat_masuk),

]
