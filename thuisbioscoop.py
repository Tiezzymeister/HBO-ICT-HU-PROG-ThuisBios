import requests
import xmltodict
import datetime
from tkinter import *


def get_films():
    api_url = 'http://api.filmtotaal.nl/filmsoptv.xml?apikey=4520nc22kzoks8g1nbi4lihxyuu6z0ng&dag=0-0-0&sorteer=0'
    api_url = list(api_url)
    now = datetime.datetime.today()
    api_url[83] = now.strftime("%d")
    api_url[85] = now.strftime("%m")
    api_url[87] = now.strftime("%Y")
    api_url = "".join(str(item) for item in api_url)
    response = requests.get(api_url)
    xmldictionary = xmltodict.parse(response.text)
    films = xmldictionary["filmsoptv"]["film"]
    print(films)                                            #
    for film in films:                                      #
        if film["titel"] and film["regisseur"] is not None: #DIT ME+OET ERUIT GEHAALD WORDEN
            print(film["titel"] + " - " + film["regisseur"])#
            
            
def inlogbezoeker():
    print("bezoekertest")
    
    
def inlogaanbieder():
    print("aanbiedertest")
root = Tk()

bezoeker = Button(master=root, text="bezoeker", command=inlogbezoeker)
bezoeker.pack(side=LEFT, pady=10)
aanbieder = Button(master=root, text="aanbieder", command=inlogaanbieder)
aanbieder.pack(side=RIGHT, pady=10)

root.mainloop()







get_films()
