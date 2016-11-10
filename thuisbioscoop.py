import requests
import xmltodict
import datetime
from tkinter import *


class InlogScherm:

    def __init__(self, master):
        frame = Frame(master)
        frame.pack()

        self.bezoekerButton = Button(frame, text = "Bezoeker", command = self.inlogbezoeker)
        self.bezoekerButton.pack(side = LEFT)

        self.aanbiederButton = Button(frame, text = "Aanbieder", command = self.inlogaanbieder)
        self.aanbiederButton.pack(side = LEFT)

        self.quitButton = Button(frame, text = "Afsluiten", command = frame.quit)
        self.quitButton.pack(side = LEFT)

    def inlogbezoeker(self):
        print("Bezoekertest.")

    def inlogaanbieder(self):
        print("Aanbiedertest.")


root = Tk()
programma = InlogScherm(root)
root.mainloop()

# def get_films():
#     api_url = 'http://api.filmtotaal.nl/filmsoptv.xml?apikey=4520nc22kzoks8g1nbi4lihxyuu6z0ng&dag=0-0-0&sorteer=0'
#     api_url = list(api_url)
#     now = datetime.datetime.today()
#     api_url[83] = now.strftime("%d")
#     api_url[85] = now.strftime("%m")
#     api_url[87] = now.strftime("%Y")
#     api_url = "".join(str(item) for item in api_url)
#     response = requests.get(api_url)
#     xmldictionary = xmltodict.parse(response.text)
#     films = xmldictionary["filmsoptv"]["film"]
#     print(films)                                            #
#     for film in films:                                      #
#         if film["titel"] and film["regisseur"] is not None: # dit verwijderen
#             print(film["titel"] + " - " + film["regisseur"])#
#
# get_films()
