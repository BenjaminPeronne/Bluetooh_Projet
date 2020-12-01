# -*-coding:Latin-1 -*-

#Fenetre de communication avec un pad (clavier) bluetooth

# Fichier : sendGetSerial.py
# Auth : 
# Modified by : Benjamin Peronne

# Importation des modules (packages)
from Tkinter import * # On importe Tkinter
import tkMessageBox  # On importe le module messagebox
import serial   # On importe le module de communication serie version pyserial-3.4
import time     # On importe le module temps


#-------------------------------------------------------#
#                    Code Application                   #
#-------------------------------------------------------#


# Declaration des variables globales
comEtablie=False
ser1=0

# Les fonctions de l'application
def scanPort():
        # Scan les ports. retourne une liste des noms des ports
    available = [""]
    for i in range(25):
        try:
            port = "COM"+str(i)
            s = serial.Serial(port)
            available.append(s.portstr)
            s.close()
        except serial.SerialException:
            pass
    return available

def quitter():
        # Termine l'application et ferme la fenêtre
    global comEtablie
	
    if comEtablie==True: # Ne deconnecte que si la connexion reseau est etablie
        deconnecter()
    fenetre.destroy()   # Ferme la fenêtre

def connecter():
       # Connection à la cible   
    global comEtablie
    global ser1

    E5.delete(0, END)
    E5.insert(END,"En attente de connexion ...")
    fenetre.update()  # Rafraichissement de l'affichage de la fenetre

    try:
        ser1 = serial.Serial(E3.get(),timeout=1)    # Ouverture du port serie de communication
        print (ser1.portstr)       # Verifie qu'elle port est vraiment utiliser
        E5.delete(0, END)
        E5.insert(END,"connectée")
        comEtablie=True
        Benvoyer1.configure(state=NORMAL)
        Bconnecter.configure(state=DISABLED)
        Bdeconnecter.configure(state=NORMAL)
    except serial.SerialException:
        E5.delete(0, END)
        E5.insert(END,"erreur ouverture port %s" % E3.get())

def deconnecter():
      # Deconnection de la cible    
    global comEtablie
    global ser1

    ser1.close()             # Fermeture port
    E5.delete(0, END)
    E5.insert(END,"déconnectée")
    comEtablie=False
    Benvoyer1.configure(state=DISABLED)
    Bconnecter.configure(state=NORMAL)
    Bdeconnecter.configure(state=DISABLED)

def envoi(valString):
    """
    transmet les données sur TXD
    valString : (str) : valeur sous forme de chaine à envoyer
    """
    global comEtablie
    global ser1

    if comEtablie==True:
        ser1.write(valString.encode())
        time.sleep(0.3) 


def recevoir():
    # Recoit les données sur RXD
    global ser1
    global comEtablie

    if comEtablie == True:
        if ser1.inWaiting() != 0 :
            valrecue = ser1.readline()    # Lecture de 10 octets max dans le buffer de reception
            # Valrecue = valrecue.decode('ascii')
            E1.delete(0, END)
            E1.insert(END,valrecue)
        else:
            pass
    else:
        pass
    fenetre.after(500,recevoir) # Mise à jour toutes les 500 ms

def about():
    tkMessageBox.showinfo("About", "This is a build version of serial bluetooth communication\nAuth : Benjamin Peronne")


# Le programme principal
fenetre = Tk()  # Création de la fenêtre principale
fenetre.title("Moniteur connexion bluetooth")   # Titre ecrit dans la fenetre
fenetre.resizable(width=False, height=False)

#La zone d'affichage
LF1=LabelFrame(fenetre,text="Valeurs recues", padx=5, pady=10)
LF1.pack(fill="both", expand="yes")

L1=Label(LF1, text="Valeur reçue :  ")
L1.grid(row=0, column=0)
E1 = Entry(LF1,width=30)
E1.grid(row=0, column=1, sticky=E, padx=5, pady=10)
E1.insert(END,"")


#La zone de saisie
LF2=LabelFrame(fenetre,text="Commandes", padx=5, pady=10)
LF2.pack(fill="both", expand="yes")

L2=Label(LF2, text="Valeur envoyée : ")
L2.grid(row=0, column=0, sticky=W)
E2=Entry(LF2, width=20)
E2.grid(row=0, column=1, sticky=E, padx=5, pady=10)

Benvoyer1=Button(LF2, text="Envoyer", state=DISABLED, command=lambda :envoi(E2.get()))
Benvoyer1.grid(row=0, column=2, padx=5, pady=10, sticky=E)


#La zone de configuration
LF3=LabelFrame(fenetre,text="Configuration", padx=5, pady=10)
LF3.pack(fill="both", expand="yes")
L4=Label(LF3, text="Numéro port serie")
L4.grid(row=0, column=0, sticky=W)

optionList = scanPort()

E3 = StringVar()
E3.set(optionList[0])
om = OptionMenu (LF3,E3, *optionList)
om.grid(row=0, column=1, sticky=E, padx=5, pady=10)

L6=Label(LF3, text="Etat")
L6.grid(row=2, column=0, sticky=W)
E5 = Entry(LF3,width=40)
E5.grid(row=2, column=1, columnspan=2, sticky=E, padx=5, pady=10)
E5.insert(END,"déconnectée")
Bconnecter=Button(LF3, text="Connecter",command=connecter)
Bconnecter.grid(row=3, column=0, padx=5, pady=10)
Bdeconnecter=Button(LF3, text="Deconnecter", state=DISABLED, command=deconnecter)
Bdeconnecter.grid(row=3, column=1, padx=5, pady=10)
Babout=Button(LF3, text="About", command=about)
Babout.grid(row=3, column=2, padx=5, pady=10)

recevoir()  # La fonction qui recupere les donnees presentes en reception RXD

fenetre.protocol("WM_DELETE_WINDOW", quitter) # Execute la fonction quitter() si la croix rouge est clquée
fenetre.mainloop()
