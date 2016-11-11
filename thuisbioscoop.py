import requests
import xmltodict
import datetime
import csv
import random
import time
from tkinter import *
from tkinter.messagebox import showinfo


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
    return films


def get_code():
    digit1 = random.randrange(0, 10)
    digit2 = random.randrange(0, 10)
    digit3 = random.randrange(0, 10)
    digit4 = random.randrange(0, 10)
    code = str(digit1) + str(digit2) + str(digit3) + str(digit4)
    return code


tiesfilms = ["Ties"]
christiaanfilms = ["Christiaan"]
burakfilms = ["Burak"]
haroutfilms = ["Harout"]
naam_en_email = []
filmlst = []
code = get_code()
tijden = []


def films_delen():
    templist = []
    filmslist = []
    with open("films.csv", "r", newline="") as filmsfile:
        reader = csv.reader(filmsfile, delimiter=";")
        for row in reader:
            templist.append(row)
        for item in templist:
            filmslist.append(item[0])
    try:
        tiesfilms.append(filmslist[0])
        tiesfilms.append(filmslist[8])
    except IndexError:
        pass
    try:
        christiaanfilms.append(filmslist[1])
        christiaanfilms.append(filmslist[9])
    except IndexError:
        pass
    try:
        burakfilms.append(filmslist[2])
        burakfilms.append(filmslist[10])
    except IndexError:
        pass
    try:
        haroutfilms.append(filmslist[3])
        haroutfilms.append(filmslist[11])
    except IndexError:
        pass

    with open("aanbieders.csv", "w", newline="") as aanbiedersCSV:
        schrijver = csv.writer(aanbiedersCSV, delimiter=";")
        schrijver.writerow(tiesfilms)
        schrijver.writerow(christiaanfilms)
        schrijver.writerow(burakfilms)
        schrijver.writerow(haroutfilms)


def aangeboden_films():
    templist = []
    templist2 = []
    aangeboden = []
    with open("aanbieders.csv", "r", newline="") as aanbiedersfile:
        reader = csv.reader(aanbiedersfile, delimiter=";")
        for row in reader:
            templist.append(row[1:])
        for item in templist:
            templist2.append(item)
        for sublist in templist2:
            for val in sublist:
                aangeboden.append(val)
    return aangeboden


def bezoekersties():
    naam = naam_en_email[0]
    email = naam_en_email[1]
    film = filmlst[0]
    begintijd = tijden[0]
    try:
        with open("bezoekersties.csv", "a", newline="") as myCSVFile:
            writer = csv.writer(myCSVFile, delimiter=";")
            writer.writerow((begintijd, naam, film, code, email))
    except FileNotFoundError:
        with open("bezoekersties.csv", "w", newline="") as myCSVFile:
            writer = csv.writer(myCSVFile, delimiter=";")
            writer.writerow((begintijd, naam, film, code, email))


def bezoekerschristiaan():
    naam = naam_en_email[0]
    email = naam_en_email[1]
    film = filmlst[0]
    begintijd = tijden[0]
    try:
        with open("bezoekerschristiaan.csv", "a", newline="") as myCSVFile:
            writer = csv.writer(myCSVFile, delimiter=";")
            writer.writerow((begintijd, naam, film, code, email))
    except FileNotFoundError:
        with open("bezoekerschristiaan.csv", "w", newline="") as myCSVFile:
            writer = csv.writer(myCSVFile, delimiter=";")
            writer.writerow((begintijd, naam, film, code, email))


def bezoekersburak():
    naam = naam_en_email[0]
    email = naam_en_email[1]
    film = filmlst[0]
    begintijd = tijden[0]
    try:
        with open("bezoekersburak.csv", "a", newline="") as myCSVFile:
            writer = csv.writer(myCSVFile, delimiter=";")
            writer.writerow((begintijd, naam, film, code, email))
    except FileNotFoundError:
        with open("bezoekersburak.csv", "w", newline="") as myCSVFile:
            writer = csv.writer(myCSVFile, delimiter=";")
            writer.writerow((begintijd, naam, film, code, email))


def bezoekersharout():
    naam = naam_en_email[0]
    email = naam_en_email[1]
    film = filmlst[0]
    begintijd = tijden[0]
    try:
        with open("bezoekersharout.csv", "a", newline="") as myCSVFile:
            writer = csv.writer(myCSVFile, delimiter=";")
            writer.writerow((begintijd, naam, film, code, email))
    except FileNotFoundError:
        with open("bezoekersharout.csv", "w", newline="") as myCSVFile:
            writer = csv.writer(myCSVFile, delimiter=";")
            writer.writerow((begintijd, naam, film, code, email))


class ThuisBioscoop:

    def __init__(self, master):
        frame = Frame(master)
        frame.pack()
        self.bezoekerButton = Button(frame, text="Bezoeker", command=self.inlogbezoeker)
        self.bezoekerButton.pack(side=LEFT)

        self.aanbiederButton = Button(frame, text="Aanbieder", command=self.inlogaanbieder)
        self.aanbiederButton.pack(side=LEFT)

        self.quitButton = Button(frame, text="Afsluiten", command=frame.quit)
        self.quitButton.pack(side=LEFT)

    def inlogbezoeker(self):
        try:
            self.klaar()
        except:
            pass
        self.instruction = Label(text="Naam: ")
        self.instruction.pack(padx=5, pady=5)
        self.bezoekerNaam = Entry()
        self.bezoekerNaam.pack(padx=5, pady=5)
        self.instruction2 = Label(text="e-Mail: ")
        self.instruction2.pack(padx=5, pady=5)
        self.bezoekerEmail = Entry()
        self.bezoekerEmail.pack(padx=5, pady=5)
        self.submitButton = Button(text="Volgende", command=self.filmkeuze)
        self.submitButton.pack(padx=5, pady=5)

    def filmkeuze(self):
        naam = self.bezoekerNaam.get()
        email = self.bezoekerEmail.get()
        if naam == "" or email == "" or "@" not in email:
            showinfo(title="fout", message="Ongeldige naam of email, probeer het nog eens")
            return
        else:
            naam_en_email.append(naam)
            naam_en_email.append(email)
            self.instruction.destroy()
            self.instruction2.destroy()
            self.bezoekerNaam.destroy()
            self.bezoekerEmail.destroy()
            self.submitButton.destroy()
            pass
        self.instruction = Label(text="Toets het nummer van de film in")
        self.instruction.pack(padx=10, pady=10)
        self.filmNummer = Entry()
        self.filmNummer.pack(padx=10, pady=10)
        self.films = Label(text="1. " + aangeboden[0] + "\n" + "2. " + aangeboden[1] + "\n" + "3. " + aangeboden[2] + "\n" + "4. " + aangeboden[3] + "\n" + "5. " + aangeboden[4] + "\n" + "6. " + aangeboden[5] + "\n" + "7. " + aangeboden[6])
        self.films.pack(padx=10, pady=10)
        self.submitButton = Button(text="Volgende", command=self.filminfo)
        self.submitButton.pack(padx=20, pady=20)

    def filminfo(self):
        try:
            filmgetal = int(self.filmNummer.get())
            if filmgetal <= 0:
                filmgetal = 12,6
        except ValueError:
            showinfo(title="fout", message="Vul een heel positief getal in in cijfers!")
            return

        try:
            film = aangeboden[filmgetal-1]
            filmlst.append(film)
        except IndexError:
            showinfo(title="fout", message="Kies een nummer uit de luist!")
            return
        except TypeError:
            showinfo(title="fout", message="Vul een heel positief getal in in cijfers!")
            return

        tijden_epoch = []
        with open("films.csv", "r", newline="") as filmsfile:
            reader = csv.reader(filmsfile, delimiter=";")
            for row in reader:
                if row[0] == film:
                    tijden_epoch.append(row[1:3])
        for item in tijden_epoch:
            tijden_epoch = item
        self.instruction.destroy()
        self.filmNummer.destroy()
        self.films.destroy()
        self.submitButton.destroy()

        begintijd = time.strftime('%H:%M:%S %d-%m-%Y ', time.localtime(int(tijden_epoch[0])))
        eindtijd = time.strftime('%H:%M:%S %d-%m-%Y ', time.localtime(int(tijden_epoch[1])))
        tijden.append(begintijd)
        tijden.append(eindtijd)
        if film in tiesfilms:
            bezoekersties()
            aanbieder = "Ties"
        elif film in christiaanfilms:
            bezoekerschristiaan()
            aanbieder = "Christiaan"
        elif film in burakfilms:
            bezoekersburak()
            aanbieder = "Burak"
        elif film in haroutfilms:
            bezoekersharout()
            aanbieder = "Harout"

        self.infolabel = Label(text="Film: " + film + "\n" + "Begintijd: " + begintijd + "\n" + "Eindtijd: " + eindtijd + "\n" + "Deze film wordt mede mogelijk gemaakt door: " + aanbieder + "\n" + "Uw unieke code is:" + code)
        self.infolabel.pack(padx=10, pady=10)
        self.klaarButton = Button(text="Klaar", command=self.klaar)
        self.klaarButton.pack(padx=10, pady=10)

    def klaar(self):
        self.infolabel.destroy()
        self.klaarButton.destroy()

    def inlogaanbieder(self):
        self.instruction = Label(text="Naam: ")
        self.instruction.pack(padx=5, pady=5)
        self.bezoekerNaam = Entry()
        self.bezoekerNaam.pack(padx=5, pady=5)
        self.instruction2 = Label(text="e-Mail: ")
        self.instruction2.pack(padx=5, pady=5)
        self.bezoekerEmail = Entry()
        self.bezoekerEmail.pack(padx=5, pady=5)
        self.submitButton = Button(text="Volgende", command=self.optiemenu)
        self.submitButton.pack(padx=5, pady=5)

    def optiemenu(self):
        print("check password")



films_on_tv = get_films()
films_delen()
aangeboden = aangeboden_films()


root = Tk()
programma = ThuisBioscoop(root)
root.mainloop()

with open("films.csv", "w", newline="") as bestand:
    writer = csv.writer(bestand, delimiter=';')
    for film in films_on_tv:
        if film["titel"] and film["starttijd"] and film["eindtijd"] and film["zender"] is not None:
            writer.writerow((film["titel"], film["starttijd"], film["eindtijd"], film["zender"]))

# with open("films.csv", "a", newline="") as bestand:
#     writer = csv.writer(bestand, delimiter=';')
#     for film in films_on_tv_morgen:
#         if film["titel"] and film["starttijd"] and film["eindtijd"] and film["zender"] is not None:
#             writer.writerow((film["titel"], film["starttijd"], film["eindtijd"], film["zender"]))
