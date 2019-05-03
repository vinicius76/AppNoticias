from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(Noticia,Pessoa,Tag)
class NoticiaAdmin(admin.ModelAdmin):
    pass