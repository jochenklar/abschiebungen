from django.core.management.base import BaseCommand
from data.models import *



class Command(BaseCommand):


    def handle(self, *args, **options):
        items = ZurueckweisungSeewegGruende.objects.all()
        for i in items:
            c = i.nationalitaet
            
            try:
                country = Country.objects.get(german_name = c)
                i.nationalitaet_country = country
                i.save()
            except Exception, e:
                print c
                print e
                pass