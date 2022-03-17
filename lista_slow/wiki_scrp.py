import requests 

def rlist():

    wikiraw = requests.get(link)
    wikitext = wikiraw.text

    poczatek = wikitext.find('Poniżej wyświetlono')
    koniec = wikitext.find('<div class="printfooter">')

    wikitext = wikitext[poczatek:koniec]

    wikirawlist = wikitext.split("</a>")

    return wikirawlist    

def tlist(rawlist):

    wikilist = []
    
    for l in rawlist:
    
        l = l.rsplit('>')
        dlugosc_l = len(l)
        wikilist.append(l[dlugosc_l - 1])
        
    wikitruelist = []
    
    for w in wikilist:
        w = w.replace("następna strona", " ")
        w = w.replace("poprzednia strona", " ")
        w = w.strip()
        if w:
            wikitruelist.append(w)

    return wikitruelist

def zmianalinku():
    
    lin = str(rlist()).split('>następna strona')
    lind = len(lin)
    lin = str(lin[lind - 2]).rsplit('(<a href="')
    lind = len(lin)
    lin = lin[lind-1]
    
    lin = lin.split('" title')
    
    lin = "https://pl.wiktionary.org"+str(lin[0])
    
    lin = lin.replace('amp;', '')

    return lin

link = 'https://pl.wiktionary.org/w/index.php?title=Kategoria:J%C4%99zyk_polski_-_przymiotniki&from=A#mw-pages'

i = 1
for i in range(20000):
    for l in (tlist(rlist())):
        print(l)
    if len(tlist(rlist())) != 200:
        break
    else:
        link = zmianalinku()

        
        


