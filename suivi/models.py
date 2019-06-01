from django.db import models
from django.contrib.auth.models import AbstractUser, User, PermissionsMixin
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse
from django.contrib.auth.models import User, Group
# Create your models here.


class Division(models.Model):
    
    division_nom = models.CharField(max_length=50, blank = True, null = True) 

    def __str__(self):
        return self.division_nom
     


class PagesPage(models.Model):

    
    title = models.CharField(max_length=60)
    permalink = models.CharField(unique=True, max_length=12)
    bodytext = models.TextField()

    def __str__(self):
        return self.title


class Pied(models.Model):
    
    pied_nom = models.CharField( max_length=10)

    def __str__(self):
        return self.pied_nom
    

class TypeCli(models.Model):
    
    typ_nom = models.CharField(max_length=50)

    def __str__(self):
        return self.typ_nom
     


class Postes(models.Model):
    
    pos_nom = models.CharField( max_length=50)  
    pos_type = models.CharField(max_length=50)  

    def __str__(self):
        return self.pos_nom
        
class Section(models.Model):

    sec_nom = models.CharField( max_length=5)  
    sec_age_max = models.IntegerField 

    def __str__(self):
        return self.sec_nom
     
class Client(AbstractUser):
    # TODO créer une liste de choix pour client perso etc...
    ENTR =[]
    FOOTBALLEUR = 'FOOT'
    ENTRAINEUR = 'ENTR'
    ADMINI = 'ADMI'
    CATU_CHOICES =(
        (FOOTBALLEUR, 'Footballeur'),
        (ENTRAINEUR, 'Entraineur'),
        (ADMINI, 'Admin')
        )
    catu = models.CharField(max_length=4,
        choices = CATU_CHOICES,
        default= FOOTBALLEUR,
        verbose_name ='Catégorie accès:'
    ) 
    nom = models.CharField('Nom', max_length = 50)
    prenom = models.CharField(max_length = 50)
    email = models.EmailField(unique = True)
    naissance = models.DateField(auto_now = False, blank = True, null = True)
    adresse = models.CharField(max_length=250, blank = True)  
    codepos = models.IntegerField(blank=True, null=True)  
    ville = models.CharField(blank=True, null=True, max_length=50)  
    telephone = models.CharField(blank=True, null=True, max_length=10)  
    club = models.CharField(blank=True, null=True, max_length=50)  
    club_ville = models.CharField(blank=True, null=True, max_length=50)  
    pos = models.ForeignKey(Postes, blank=True, null=True, on_delete = models.SET_NULL, verbose_name ='Poste')  
    sec = models.ForeignKey(Section, blank=True, null=True, on_delete = models.SET_NULL, verbose_name ='Section')  
    division = models.ForeignKey(Division, blank=True, null=True, on_delete = models.SET_NULL)  
    pied = models.ForeignKey(Pied, blank=True, null=True, on_delete = models.SET_NULL)  
    typ = models.ForeignKey(TypeCli, blank=True, null=True, on_delete = models.SET_NULL,verbose_name ='Type de client')
    

    def get_absolute_url(self):
        return reverse("client_detail", kwargs={"pk": self.pk})

    def __str__(self): 
        return '{} {}'.format(self.last_name, self.first_name)
        

    @classmethod
    def GET_ENTR(cls):
        ent = [e for e in Client.objects.all() if e.catu == 'ENTR']
        return ent
   
           
class Typsuivi(models.Model):

    typsuivi_nom = models.CharField( max_length=25)

    def __str__(self):
        return self.typsuivi_nom
    

class Suivobs(models.Model):
    
    suivobs_date = models.DateField(auto_now = True)  
    suivobs_theme = models.CharField( max_length=50, blank=True, null=True)  
    suivobs_travail = models.TextField(max_length=50, blank=True, null=True)  
    suivobs_observation = models.TextField(max_length=500)  
    suivobs_axeprogres = models.TextField(max_length=50)  
    suivobs_video = models.CharField( max_length=255, blank=True, null=True)  
    suivobs_resultat = models.CharField( max_length=25, blank=True, null=True)  
    suivobs_but = models.IntegerField( blank=True, null=True)  
    suivobs_passe = models.IntegerField(blank=True, null=True)  
    typsuivi = models.ForeignKey(Typsuivi,  blank=True, null=True, on_delete = models.SET_NULL)
    coach = models.ForeignKey(Client, related_name="Entraineur", blank=True, null=True, on_delete = models.SET_NULL,limit_choices_to={'is_staff':True})
    joueur = models.ForeignKey(Client, related_name="Joueur", blank=True, null=True, on_delete = models.SET_NULL,limit_choices_to={'is_staff':False})
    
    def __str__(self):
        suivi = {'date': self.suivobs_date, 'coach': self.coach, 'joueur': self.joueur}
        return suivi

    def get_absolute_url(self):
        # TODO changer pk en autre chose et créer l'url correspondante pour detail suivi joueur
        return reverse("suivi_detail", kwargs={"pk": self.id})      
    """
    def GETSUIVIBYCLIENT(self, clientid):
        lstclisuivi = []
        s =""
        # [s for s in Suivobs.objects.all() if s.id == clientid]
        for s in Suivobs.objects.all():
            if s.id == clientid:
                lstclisuivi.append(s)
        return lstclisuivi
    """

class Concerne(models.Model):
        
    suivobs = models.ForeignKey(Suivobs, blank = True, null = True, on_delete = models.SET_NULL)  
    cli = models.ForeignKey(Client, blank = True, null = True, on_delete = models.SET_NULL ) 

    


    
        