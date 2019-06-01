from django.contrib import admin
from .models import Page
from .forms import ContactForm

# Register your models here.
class PageAdmin(admin.ModelAdmin):
    list_display = ('title',)
    ordering = ('title',)
    search_fields = ('title',)

admin.site.register(Page, PageAdmin)

