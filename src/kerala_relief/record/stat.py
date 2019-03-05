import requests
from bs4 import BeautifulSoup
def records():
    url="https://donation.cmdrf.kerala.gov.in/index.php/Settings/transparency#expenditure"
    r=requests.get(url)
    soup=BeautifulSoup(r.content,"lxml")
    #print(soup)
    #print(soup.prettify())
    # x=soup.find_all("table",{"class":"table table-responsive table-bordered table-striped"})
    x=soup.find_all("td",{"bgcolor":"#85C1D9"})
    y=soup.find_all("td")
    m=[]
    d=[]
    e=[]
    f=[]
    g=[]
    n=[]
    ff=0
    for i in range(0,3):
        d.append(x[i].text)
    for i in range(3,5):
        e.append(x[i].text)
    for i in range(5,7):
        f.append(x[i].text)
    for i in range(7,len(x)):
        g.append(x[i].text)
    for i in range(23,len(y)):
        m.append(y[i].text)



    return d,e,f,g,m
