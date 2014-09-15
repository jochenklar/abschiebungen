import urllib2
from BeautifulSoup import BeautifulSoup
from django.core.management.base import BaseCommand
from data.models import Country


class Command(BaseCommand):


    def handle(self, *args, **options):
        response = urllib2.urlopen('http://www.countryareacode.net/')
        soup = BeautifulSoup(response)
        tables = soup.findChildren('table')
        my_table = tables[0]        
        rows = my_table.findChildren('tr')

        for row in rows:
            country = Country.objects.create()       
            cells = row.findChildren('td')
            for cell in cells:
                if cell.findChildren('a'):
                    for a in cell.findChildren('a'):
                        if a.string:
                            country.english_name  =  a.string
                            country.save()
                
                if cell.findChildren('b'):
                    b = cell.findChildren('b')
                    if not b[0].string.startswith('+'):
                        value = b[0].string
                        if len(value) == 2:
                            country.shortcut_two = value
                            country.save()
                            print 'shortname '+ value
                        if len(value) ==3:
                            country.shortcut_three = value
                            country.save()
                            print 'short ' + value
                country.save()               
            print '---------------'

