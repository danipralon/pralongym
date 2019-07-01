from django.contrib import admin

# Register your models here.
from .models import Cliente

@admin.register(Cliente)
class ClienteAdimin(admin.ModelAdmin):
    list_display=['id','nome']