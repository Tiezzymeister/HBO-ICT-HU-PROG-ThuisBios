import requests
import xmltodict
import datetime
from tkinter import *
root = Tk()

label = Label(master=root, text='Test', background='pink')
label.pack()

root.mainloop()


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
    print(films)
    for film in films:
        if film["titel"] and film["regisseur"] is not None:
            print(film["titel"] + " - " + film["regisseur"])

def menu():
    print("Welkom, dit zijn uw opties: ")
    print("1. Ik wil inloggen als filmbezoeker of filmaanbieder.") #dit later misschien splitsen?
    print("2. Ik wil alle films van een filmaanbieder zien.")
    print("3. Ik wil het totaal aantal bezoekers en/of het aantal bezoekers per film zien.")
    gekozenoptie = input("Kies een optie (1-3): ")
    if gekozenoptie == "1":
        aanmelden()
    if gekozenoptie == "2":
        allefilms()
    if gekozenoptie == "3":
        totalen()
    else:
        menu()
def aanmelden():
    print("Hier komt nog wat.")

def allefilms():
    print("Hier moet ook nog wat komen.")

def totalen():
    print("En ook nog wat hier...")

get_films()
menu()
