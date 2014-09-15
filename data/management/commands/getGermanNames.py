import urllib2
from BeautifulSoup import BeautifulSoup
from django.core.management.base import BaseCommand

from data.models import Country


class Command(BaseCommand):

    def handle(self, *args, **options):

        response = urllib2.urlopen('http://de.wikipedia.org/wiki/Liste_der_Kfz-Nationalit%C3%A4tszeichen')
        soup = BeautifulSoup(response)
        tables = soup.findChildren('table')

        my_table = tables[0]        
        rows = my_table.findChildren('tr')

        for row in rows:
            cells = row.findChildren('td') 
            value1 = ''
            value = ''           
            for idx,cell in enumerate(cells):                
                if idx == 1:                    
                    for a in cell.findChildren('a'):
                        value1 = a.string                        
                if idx ==2:                    
                    value = cell.string 
            try:                
                country = Country.objects.get(shortcut_two=value)
                country.german_name = value1
                country.save()
            except Exception, e:
                print value
                print e               
                pass

            
