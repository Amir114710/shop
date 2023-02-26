from django.contrib import admin
from .models import Poster


@admin.register(Poster)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('title' , 'content' , 'image')
