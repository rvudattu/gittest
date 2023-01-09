from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Quote
# Register your models here.
@admin.register(Quote)
class QuoteAdmin(admin.ModelAdmin):
    list_display = ("author", "quote")