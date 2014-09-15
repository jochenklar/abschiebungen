import urllib2
from BeautifulSoup import BeautifulSoup
import os, sys


if os.path.isfile('abschiebungen/settings.py'):
    sys.path.append(os.getcwd())
else:
    sys.exit('Error: not in the root directory of the django project.');


from data.models import Country


response = urllib2.urlopen('http://www.countryareacode.net/')
soup = BeautifulSoup(response)
tables = soup.findChildren('table')

my_table = tables[0]
#print my_table
rows = my_table.findChildren('tr')

for row in rows:
    #print len(row)    
    
    cells = row.findChildren('td')

    for cell in cells:


        if cell.findChildren('a'):
            for a in cell.findChildren('a'):
                if a.string:
                    print 'Country: ' +  a.string
        
        if cell.findChildren('b'):
            b = cell.findChildren('b')
            if not b[0].string.startswith('+'):
                value = b[0].string
                if len(value) == 2:
                    print 'shortname '+ value
                if len(value) ==3:
                    print 'short ' + value

                

       
    print '---------------'

