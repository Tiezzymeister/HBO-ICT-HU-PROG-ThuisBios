import requests
import xmltodict
import datetime
import csv
import random
import time
from tkinter import *
from tkinter.messagebox import showinfo


def get_films():
    """
    Deze code is om de informatie op te halen van films op tv en stopt het in een CSV-file
    """
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
    with open("films.csv", "w", newline="") as bestand:
        writer = csv.writer(bestand, delimiter=';')
        for film in films:
            if film["titel"] and film["starttijd"] and film["eindtijd"] and film["zender"] is not None:
                writer.writerow((film["titel"], film["starttijd"], film["eindtijd"], film["zender"]))


def get_code():
    """
    Deze coce maakt een random code voor de bezoeker
    """
    digit1 = random.randrange(0, 10)
    digit2 = random.randrange(0, 10)
    digit3 = random.randrange(0, 10)
    digit4 = random.randrange(0, 10)
    rcode = str(digit1) + str(digit2) + str(digit3) + str(digit4)
    return rcode


tiesfilms = ["Ties"]
christiaanfilms = ["Christiaan"]
burakfilms = ["Burak"]
haroutfilms = ["Harout"]
naam_en_email = []
filmlst = []
code = get_code()
tijden = []


def films_delen():
    """
    Dit stuk code verdeelt de films
    """

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
    """
    Dit stuk code maakt een lijst met alle aangeboden films
    """
    templist = []
    templist2 = []
    aangebodenlst = []
    with open("aanbieders.csv", "r", newline="") as aanbiedersfile:
        reader = csv.reader(aanbiedersfile, delimiter=";")
        for row in reader:
            templist.append(row[1:])
        for item in templist:
            templist2.append(item)
        for sublist in templist2:
            for val in sublist:
                aangebodenlst.append(val)
    return aangebodenlst


def bezoekersties():
    """
    Dit stuk code zet alle info van de bezoekers van Ties in een csv file
    """
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
    """
    Dit stuk code zet alle info van de bezoekers van Christiaan in een csv file
    """
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
    """
    Dit stuk code zet alle info van de bezoekers van Burak in een csv file
    """

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
    """
    Dit stuk code zet alle info van de bezoekers van Harout in een csv file
    """

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
    """
    Deze code zorgt voor de GUI
    """

    def __init__(self, master):
        """
        Deze code zorgt ervoor dat dat er een schermpje is met knoppen en hij initieert zichzelf ook zorgt hij ervoor dat op als je op een bepaalde knop drukt dat dan de juiste functies starten
        """
        frame = Frame(master)
        frame.pack()
        self.bezoekerButton = Button(frame, text="Bezoeker", command=self.inlogbezoeker)
        self.bezoekerButton.pack(side=LEFT)

        self.aanbiederButton = Button(frame, text="Aanbieder", command=self.inlogaanbieder)
        self.aanbiederButton.pack(side=LEFT)

        self.quitButton = Button(frame, text="Afsluiten", command=frame.quit)
        self.quitButton.pack(side=LEFT)

    def inlogbezoeker(self):

        """
        Deze code vraagt de informatie van de bezoeker en initieert de filmkeuze functie
        """

        self.clear()
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

        """
        Deze code zorgt er eerst voor dat er wordt gechecht of de gebruiker een zijn naam heeft ingevuld en hij kijkt ook of het een een geldig email adres is anders geeft hij een pop-up message en laat hij je het nog een keer invullen en als de invoer goed is gooit deleta hij de ouwe GUI en gaat hij door.
        Er wordt hierin ook een nieuwe GUI getekend die de gebruiker vraagt om een film en initeert dan de filmkeuze functie
        """
        naam = self.bezoekerNaam.get()
        email = self.bezoekerEmail.get()
        if naam == "" or email == "" or "@" not in email or "." not in email:
            showinfo(title="fout", message="Ongeldige naam of email, probeer het nog eens")
            return
        else:
            naam_en_email.append(naam)
            naam_en_email.append(email)
            self.clear()
            pass

        self.instruction = Label(text="Toets het nummer van de film in")
        self.instruction.pack(padx=10, pady=10)
        self.filmNummer = Entry()
        self.filmNummer.pack(padx=10, pady=10)
        self.films = Label(text="1. " + aangeboden[0] + "\n" + "2. " + aangeboden[1] + "\n" + "3. " + aangeboden[2] + "\n" + "4. " + aangeboden[3] + "\n" + "5. " + aangeboden[4] + "\n" + "6. " + aangeboden[5] + "\n" + "7. " + aangeboden[6])
        self.films.pack(padx=10, pady=5)
        self.submitButton = Button(text="Volgende", command=self.filminfo)
        self.submitButton.pack(padx=10, pady=2)

    def filminfo(self):
        """
        Deze code zorgt ervoor dat de gebruiker geen verkeerde getallen invoert en als het verkeerd is geeft hij een pop-op message box en moet je het opnieuw proberen
        Dan converteert hij de epoch tijd die we van de API van filmsoptv krijgen naar conventionele tijd
        Dan wordt er gecheckt wie de aanbieder is en dan wordt de informatie in de CSV voor die aanbieder geschreven
        Dan wordt de informatie weer gegeven en de als de gebruiker op klaar drukt wordt het scherm leeg gemaakt
        """
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
        self.clear()
        with open("films.csv", "r", newline="") as filmsfile:
            reader = csv.reader(filmsfile, delimiter=";")
            for row in reader:
                if row[0] == film:
                    tijden_epoch.append(row[1:3])
        for item in tijden_epoch:
            tijden_epoch = item

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

        self.infolabel = Label(text="Film: " + film + "\n" + "Begintijd: " + begintijd + "\n" + "Eindtijd: " + eindtijd + "\n" + "Deze film wordt mede mogelijk gemaakt door: " + aanbieder + "\n" + "Uw unieke code is:" + code + "\n" + "Zonder code geen toegang!!")
        self.infolabel.pack(padx=10, pady=10)
        self.klaarButton = Button(text="Klaar", command=self.clear)
        self.klaarButton.pack(padx=10, pady=10)

    def inlogaanbieder(self):
        """
        Deze code verzorgt het login scherm voor de aanbieders
        """
        self.clear()
        self.instruction = Label(text="Naam: ")
        self.instruction.pack(padx=5, pady=5)
        self.loginNaam = Entry()
        self.loginNaam.pack(padx=5, pady=5)
        self.instruction2 = Label(text="password: ")
        self.instruction2.pack(padx=5, pady=5)
        self.password = Entry()
        self.password.pack(padx=5, pady=5)
        self.submitButton = Button(text="Volgende", command=self.passwordcheck)
        self.submitButton.pack(padx=5, pady=5)

    def passwordcheck(self):
        """
        Dit stuk code checkt of de ingevulde gegevens goed zijn en geeft de gebruiker een id mee
        """
        passwords = []
        loginnaam = self.loginNaam.get()
        loginpassword = self.password.get()
        with open("logininfo.csv", "r", newline="") as logincsv:
            reader = csv.reader(logincsv, delimiter=";")
            for row in reader:
                passwords.append(row[1])
        if loginnaam == "Ties" and loginpassword == passwords[0]:
                self.clear()
                self.keuzemenu()
                self.id = 1
        elif loginnaam == "Christiaan" and loginpassword == passwords[1]:
                self.clear()
                self.keuzemenu()
                self.id = 2
        elif loginnaam == "Burak" and loginpassword == passwords[2]:
                self.clear()
                self.keuzemenu()
                self.id = 3
        elif loginnaam == "Harout" and loginpassword == passwords[3]:
                self.clear()
                self.keuzemenu()
                self.id = 4
        else:
            showinfo(title="fout", message="Naam of wachtwoord komen niet overeen met de info in ons systeem")
            return

    def keuzemenu(self):
        """
        Hier wordthet keuze menu gemaakt
        """
        self.clear()
        self.moviesButton = Button(text="Mijn films", command=self.myfilms)
        self.moviesButton.pack(padx=10, pady=10)
        self.unofferedButton = Button(text="Nog niet aangeboden films", command=self.unoffered)
        self.unofferedButton.pack(padx=10, pady=10)

    def myfilms(self):
        """
        Dit stuk code gebruikt het ID om de goed films op het scherm te vertonen
        """
        offered = []
        aanbiersfilms = []
        with open("aanbieders.csv", "r", newline="") as aanbiederscsv:
            reader = csv.reader(aanbiederscsv, delimiter=";")
            for row in reader:
                aanbiersfilms.append(row)
        if self.id == 1:
            for item in aanbiersfilms[0]:
                offered.append(item)
            try:
                showinfo(title="Aangeboden films", message="U bied deze film(s) aan " + offered[1] + " & " + offered[2])
            except IndexError:
                showinfo(title="Aangeboden films", message="U bied deze film(s) aan " + offered[1])
        elif self.id == 2:
            for item in aanbiersfilms[1]:
                offered.append(item)
            try:
                showinfo(title="Aangeboden films", message="U bied deze film(s) aan " + offered[1] + " & " + offered[2])
            except IndexError:
                showinfo(title="Aangeboden films", message="U bied deze film(s) aan " + offered[1])
        elif self.id == 3:
            for item in aanbiersfilms[2]:
                offered.append(item)
            try:
                showinfo(title="Aangeboden films", message="U bied deze film(s) aan " + offered[1] + " & " + offered[2])
            except IndexError:
                showinfo(title="Aangeboden films", message="U bied deze film(s) aan " + offered[1])
        elif self.id == 4:
            for item in aanbiersfilms[3]:
                offered.append(item)
            try:
                showinfo(title="Aangeboden films", message="U bied deze film(s) aan " + offered[1] + " & " + offered[2])
            except IndexError:
                showinfo(title="Aangeboden films", message="U bied deze film(s) aan " + offered[1])

    def unoffered(self):
        """
        Dit stuk code vergelijkt alle aangeboden films met alle films en stopt alle films die niet in de all_films voorkomen in de lijst unofferedlst en laat hem vervolgens zien
        """
        self.clear()
        all_films = []
        with open("films.csv", "r", newline="") as bestand:
            reader = csv.reader(bestand, delimiter=';')
            for row in reader:
                all_films.append(row[0])
        unofferedlst = []
        for item in all_films:
            if item not in aangeboden:
                unofferedlst.append(item)
        self.listbox = Listbox(width=50)
        self.listbox.pack()
        for item in unofferedlst:
            self.listbox.insert(END, item)
        self.doneButton = Button(text="Klaar", command=self.keuzemenu)
        self.doneButton.pack(padx=10, pady=10)

    def clear(self):
        """
        Deze fuctie gebruik ik om het scherm leg te maken zodat er weer iets nieuws weergegeven kan worden
        """
        try:
            self.infolabel.destroy()
        except AttributeError:
            pass
        try:
            self.klaarButton.destroy()
        except AttributeError:
            pass
        try:
            self.instruction.destroy()
        except AttributeError:
            pass
        try:
            self.bezoekerNaam.destroy()
        except AttributeError:
            pass
        try:
            self.instruction2.destroy()
        except AttributeError:
            pass
        try:
            self.bezoekerEmail.destroy()
        except AttributeError:
            pass
        try:
            self.submitButton.destroy()
        except AttributeError:
            pass
        try:
            self.filmNummer.destroy()
        except AttributeError:
            pass
        try:
            self.films.destroy()
        except AttributeError:
            pass
        try:
            self.instruction.destroy()
        except AttributeError:
            pass
        try:
            self.loginNaam.destroy()
        except AttributeError:
            pass
        try:
            self.instruction2.destroy()
        except AttributeError:
            pass
        try:
            self.password.destroy()
        except AttributeError:
            pass
        try:
            self.submitButton.destroy()
        except AttributeError:
            pass
        try:
            self.unofferedButton.destroy()
        except AttributeError:
            pass
        try:
            self.moviesButton.destroy()
        except AttributeError:
            pass
        try:
            self.doneButton.destroy()
        except AttributeError:
            pass
        try:
            self.listbox.destroy()
        except AttributeError:
            pass

#\/ Dit stuk code start alle functies bovenaan de pagina
get_films()
films_delen()
aangeboden = aangeboden_films()

#\/Dit stuk code zorgt ervoor dat het frame wordt gemaakt en de code in de class ThuisBioscoop wordt gebruikt en dat hij ThuisBioscoop als title heeft en 200x200 pixels is
root = Tk()
root.title("ThuisBioscoop")
root.geometry("315x265")
programma = ThuisBioscoop(root)
root.mainloop()
