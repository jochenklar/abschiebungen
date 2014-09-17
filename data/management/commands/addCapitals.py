import urllib2
from BeautifulSoup import BeautifulSoup
from django.core.management.base import BaseCommand
from data.models import Country


class Command(BaseCommand):


    def handle(self, *args, **options):
        response = urllib2.urlopen('http://www.lab.lmnixon.org/4th/worldcapitals.html')
        soup = BeautifulSoup(response)
        tables = soup.findChildren('table')
        my_table = tables[0]        
        rows = my_table.findChildren('tr')

        for row in rows:
            cells = row.findChildren('td') 
            #print cells
            country = cells[0].string
            #print country
            # s und w negativ
            try:
                c = Country.objects.get(english_name=country)
                capitel = cells[1].string
                c.capital = capitel
                c.save()
                lat = cells[2].string
                if lat:
                    if lat.endswith('S'):
                        lat = lat[:-1]
                        c.lat = float('-' + lat)
                        c.save()
                    else:
                        lat = lat[:-1]
                        c.lat = float(lat)
                        c.save()

                try: 
                    lon = cells[3].string                    
                    if lon:
                        if lon.endswith('W'):                            
                            lon = lon[:-1]
                            c.lon = float('-' + lon)
                            c.save()
                        else:
                            lon = lon[:-1]
                            c.lon = lon
                            c.save()
                except:
                    pass
                c.save()
                
            except Exception,e:
                #print country
                pass
                
