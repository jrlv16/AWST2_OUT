from .models import Client, Suivobs
from django.contrib.auth.models import User
from . models import Client, Suivobs, Concerne
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.admin.views.decorators import staff_member_required

class ClientSearchForm(forms.Form):
    search_text = forms.CharField(
        required = False,
        label = 'Chercher par nom ou prénom',
        widget = forms.TextInput(attrs={'placeholder':'Entrez le nom ou prénom '}),
    )

    search_cat = forms.CharField(
        required = False,
        label = 'Chercher par catégorie',
        widget = forms.TextInput(attrs={'placeholder':'Ex ent, foot ...'}),
    )

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'


class ClientCreationForm(UserCreationForm):
    
    class Meta(UserCreationForm):
        model = Client
        fields = ('catu', 'groups', 'username', 'password', 'first_name',
         'last_name', 'email', 'naissance', 'adresse', 'codepos',
         'ville', 'telephone', 'club', 'club_ville', 'pos', 'sec',
          'division', 'pied', 'typ')

class ClientChangeForm(UserChangeForm):
    
    class Meta(UserChangeForm):
        model = Client
        fields = ('catu', 'username', 'first_name', 'last_name',
        #  'email', 'naissance', 'adresse', 'codepos',
         'ville', 'telephone', 'club', 'club_ville', 'pos', 'sec',
          'division', 'pied', 'typ')    
        

class ClientClientChangeForm(UserChangeForm):
    
    class Meta(UserChangeForm):
        model = Client
        fields = ('username', 'first_name', 'last_name',
         'email', 'naissance', 'adresse', 'codepos',
         'ville', 'telephone', 'club', 'club_ville', 'pos', 'sec',
          'division') 

class EntraineurCreationForm(UserCreationForm):

    class Meta:
          model = Client
          fields = ('catu', 'username', 'first_name', 'last_name',
         'email', 'naissance', 'adresse', 'codepos',
         'ville', 'telephone')  


class EntraineurChangeForm(UserChangeForm):
    
    class Meta:
        model = Client
        fields = ('catu', 'username', 'first_name', 'last_name',
         'email', 'naissance', 'adresse', 'codepos',
        )
"""
class SuivobsForm(forms.ModelForm):
    
    class Meta:
        model = Suivobs
        fields = "__all__"
"""
class SuivobsCreate(forms.ModelForm):
    class Meta:
        model = Suivobs
        fields = "__all__"      

