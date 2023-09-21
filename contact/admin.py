from django.contrib import admin
from . import models
# Register your models here.


@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = 'first_name', 'last_name', 'phone', 'category'

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    ...