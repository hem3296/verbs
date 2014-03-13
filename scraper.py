import scraperwiki
import string
import urllib2
from lxml import html
import requests
#scraperwiki.sqlite.execute("drop table ccc")
#scraperwiki.sqlite.execute("create table ccc ('Meaning','Uses','url')")
#http://docs.python.org/2/library/re.html


#mylist=[]
#mylist.append("http://www.tamildiction.org/verb_dictionary/?list=1&types_of_verbs=regular_verbs")
#mylist.append("http://dictionary.reference.com/browse/sonnet")
#mylist.append("http://dictionary.reference.com/browse/sonorous")
#mylist.append("http://dictionary.reference.com/browse/soothsayer")



for index in range(1,2):
        try:
            page = requests.get("http://www.wysk.com/index/california/anaheim/A/"+str(index))
            tree = html.fromstring(page.text)
            #This will create a list of buyers:
            meaning1 = tree.xpath('//div[@class="state-cols"]/ul/li/a/text()')
            #This will create a list of prices
            uses1 = tree.xpath('//div[@class="state-cols"]/ul/li/a/@href')
            print "|".join(meaning1)
            print "|".join(uses1)
            #scraperwiki.sqlite.execute("insert into ccc values (?,?,?)",(meaning1,uses1,url))
            #scraperwiki.sqlite.commit()
        except urllib2.HTTPError, err:
            print err
            if err.getcode() == 404:
                continue #not a problem.  move on to next date.

