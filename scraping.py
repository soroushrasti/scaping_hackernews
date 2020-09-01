import requests
from bs4 import BeautifulSoup
import pdb

res=requests.get('https://news.ycombinator.com/news')
soup=BeautifulSoup(res.text,'html.parser')


links=soup.select('.storylink')
votes=soup.select('.score')
subtext=soup.select('.subtext')

def create_custome_hn(links,subtext):
    hn=[]
    for index,item in enumerate(links):
        title=links[index].getText()
        href=links[index].get('href',None)
        vote=subtext[index].select('.score')
        if len(vote):
            points=int(vote[0].getText().replace(' points',''))
            if points >99:
                hn.append({'title':title,'link':href,'vote':points})
    return hn



import pprint

pprint.pprint(create_custome_hn(links,subtext))