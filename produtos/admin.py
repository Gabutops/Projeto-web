from django.contrib import admin

from .models import Produtos, Categoria

# Register your models here.

admin.site.register(Categoria)
admin.site.register(Produtos)