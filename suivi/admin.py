from django.contrib import admin
from .models import Client
from django.contrib.auth.admin import UserAdmin

from . forms import ClientCreationForm, ClientChangeForm

class ClientAdmin(UserAdmin):
    add_form = ClientCreationForm
    form = ClientChangeForm
    model = Client
    list_display = ['last_name', 'first_name', 'email', 'catu']

admin.site.register(Client, ClientAdmin)