from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views import generic, View
from django.views.generic.detail import DetailView, SingleObjectMixin
from django.contrib.auth.mixins import(
     LoginRequiredMixin, 
     PermissionRequiredMixin,
    )
from django.views.generic.edit import (
    CreateView,
    UpdateView,
    DeleteView,
    FormView,
    )
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import PasswordResetForm
from django.urls import reverse_lazy
from django.contrib.admin.views.decorators import staff_member_required
from search_views.search import SearchListView
from search_views.filters import BaseFilter
from django.template import Context

from . models import Client, Concerne, Division, Suivobs, TypeCli
from . forms import (
    ClientCreationForm,
    ClientChangeForm,
    ClientClientChangeForm,
    EntraineurCreationForm,
    EntraineurChangeForm,
    ClientSearchForm,
    SuivobsCreate,
    )

# Create your views here.


class ClientFilter(BaseFilter):
    search_fields = {
        'search_text': ['last_name', 'first_name'],
        'search_cat': ['catu'],
        }


class ClientListView(SearchListView, LoginRequiredMixin):
    template_name = "suivi/client_list.html"
    model = Client
    paginate_by = 10
    ordering =('last_name', 'catu')
    form_class = ClientSearchForm
    filter_class = ClientFilter
    context = Context({'user_id': User.id, 'client_id': Client.id})
    Cid = Client.id
    # TODO à ordonner pour éviter erreur


class ClientDetailView(LoginRequiredMixin, DetailView):
    model = Client
    fields = ('username', 'first_name', 'last_name',
              'email', 'naissance', 'adresse', 'codepos',
              'ville', 'telephone', 'club', 'club_ville', 'pos', 'sec',
              'division')


class ClientCreate(LoginRequiredMixin, CreateView):
    model = Client
    form_class = ClientCreationForm


class ClientUpdate(LoginRequiredMixin, generic.UpdateView):
    model = Client
    form_class = ClientChangeForm


class ClientDelete(LoginRequiredMixin, DeleteView):
    model = Client
    fields = '__all__'


class SuiviByClientListView(LoginRequiredMixin, generic.ListView):
    model = Concerne
    template_name = 'suivi/suivobs_byclient_list.html'
    fields =('suiviobs.suivobs_date', 'suiviobs.typsuivi')
    ordering = ('suiviobs.suivobs_date')
    paginate_by = 10    


class ClientClientUpdate(LoginRequiredMixin, generic.UpdateView):
    model = Client
    form_class = ClientClientChangeForm 
     

# ###################################
# ########  PERSONNEL  ##############
# ###################################


class EntraineurCreate(LoginRequiredMixin, CreateView):
    model = Client
    form_class = EntraineurCreationForm


class EntraineurDetailView(LoginRequiredMixin, DetailView):
    model = Client
    fields = ('username', 'first_name', 'last_name',
              'email', 'naissance', 'adresse', 'codepos',
              'ville', 'telephone')


class EntraineurUpdate(LoginRequiredMixin, generic.UpdateView):
    model = Client
    form_class = EntraineurChangeForm


class EntraineurDelete(LoginRequiredMixin, DeleteView):
    model = Client
    fields = '__all__'

# ########################################
# #### SUIVI JOUEURS #####################
# ########################################   


class SuivobsCreate(LoginRequiredMixin, CreateView):
    model = Suivobs
    fields = "__all__"
    form = SuivobsCreate


class SuivobsDetailView(DetailView):
    model = Suivobs
    fields = "__all__"


class SuivobsList(LoginRequiredMixin, generic.ListView):

    # on nomme l'objet qui sera renvoyé
    context_object_name = "suivobslist"
    # requête qui récupère la liste de tous les objets "suivi"
    queryset = Suivobs.objects.all()

    # modèle utilisé équivalent table de bdd

    model = Suivobs
    # template utilisé
    template_name = 'suivi/suivobs_list.html'
    # liste des champs qui seront affichés
    fields =('suivobs.suivobs_date', 'suivobs.typsuivi', 'suivobs.joueur')
    # instruction de rangement par ordre chronologique inverse

    ordering = ('-suivobs_date')

    # affichage de liste limité à 10 éléments par page 
    paginate_by = 10    


class SuiviByClientListView(SuivobsList):

    template_name = 'suivi/suivobs_byclient_list.html'

    # on filtre la liste sur l'id de l'utilisateur
    def get_queryset(self):
        return Suivobs.objects.filter(
            joueur=self.request.user.id).order_by('-suivobs_date')


class SuiviByClientEntrListView(SuivobsList):

    # on modifie le template d'affichage
    template_name = 'suivi/suivobs_ent_byclient_list.html'

    # on modifie la requête pour filtrer sur l'id passée en argument
    def get_queryset(self):
        return Suivobs.objects.filter(
            joueur=self.kwargs.get('pk')).order_by('-suivobs_date')


class MyPasswordReset(FormView):
    email_template_name = 'templates/registration/password_reset_email.html'
    form_class = PasswordResetForm
    from_email = 'foot@footexperts.fr'
    success_url = 'password_reset_done'
    template_name = 'password_reset_form.html'
