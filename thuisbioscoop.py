from tkinter import *
root = Tk()

label = Label(master=root, text='Test', background='pink')
label.pack()

root.mainloop()

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

menu()
