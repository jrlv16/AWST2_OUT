from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
"""
cette commande est créée pour être utilisée pour l'hébergement distant,
sur AWS on ne peut pas éxécuter de commande sans passer par le site qui y est hébergé
dons ce cas on ne peut créer de compte permettant d'accéder à l'admin,
on va donc lancer cette commande en même temps que le déploiement du site
"""
class Command(BaseCommand):

    def handle(self, *args, **options):
        if not User.objects.filter(username="rwf").exists():
            User.objects.create_superuser("rwf", "jl062705@sfr.fr", "culneaj")