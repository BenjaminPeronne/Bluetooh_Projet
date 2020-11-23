# Bluetooh_Projet

<div align='center' style='font-size: 30px;'>
    Analysis of the need
</div>

* Communication application with a Bluetooth keyboard allowing the entry of mathematical characters (Python language, Tkinter Modules, Pyserial).

* From a keyboard connected in Bluetooth with the computer, retrieve the code of the keys typed and integrate the mathematical symbols in the text area of the application.

<div align='center' style='font-size: 30px;'>
    How to start
</div>

## Prerequisite

The first thing is to install PyBluez,a bluetooth module, Open a terminal (command prompt on Windows) and enter :

```
pip install pybluez
```

Then you need the tkinter module, in order to be able to create a graphical interface :

```
pip install tkinter
```

We now import our necessary module

```python
# Importation
from Tkinter import * # On importe Tkinter
import tkMessageBox, tkFileDialog, Tkconstants # On importe le module messagebox et filedialog
import serial # On importe le module de communication serie version pyserial-3.4
import time # On importe le module temps
import codecs
import tkFont
```

## *Main Code*

```python
#-------------------------------------------------------#
# Code Application #
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

def connecter():
# Connection Ã  la cible
global comEtablie
global ser1

try:
ser1 = serial.Serial("COM3",timeout=1) #Configurer le com manuellement
print "connexion etablie"

comEtablie=True

except serial.SerialException:
print "erreur de connexion"

def deconnecter():
# Deconnection de la cible
global comEtablie
global ser1

ser1.close()

comEtablie=False

def configuration(valString):
"""
valString : (str) : valeur sous forme de chaine à envoyer
"""
global comEtablie
global ser1

if comEtablie==True:
ser1.write(valString.encode())
time.sleep(0.3)

def NewFile():
"""permet d'afficher a Ã  l'écran un message d'information sur une ouvelle fenÃªtre"""
tkMessageBox.showinfo("New File")

def about():
tkMessageBox.showinfo("About", "This is a build version of serial bluetooth communication\nAuth : Benjamin Peronne")

def Open():
"""permet d'ouvrir un fichier extérieur dans la fenêtre
fichier = open("data.txt", "a")
fichier.write("Bonjour monde")
fichier.close()
fen1.filename
"""
global chemin_fichier
chemin_fichier= tkFileDialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("text files","*.txt"),("all files","*.*")))
print (chemin_fichier)
mon_fichier = open(chemin_fichier, "r")
contenu = mon_fichier.read()
print(contenu)
textW.insert(END,contenu)
mon_fichier.close()

def Configuration(profil):
"""permet d'acceder au profil demander celon l'odre réseau"""
tkMessageBox.showwarning(profil)

def Save():
global chemin_fichier
contenu=textW.get("1.0",END)
print contenu
mon_fichier = open(chemin_fichier, "w")
mon_fichier.write(contenu)
mon_fichier.close()

def recevoir():
# Recoit les données sur RXD
global ser1
global comEtablie
profilN1=["∫","profil1","∞","≤","≥","√","∈","∉","∅","∩","∪","∑"]
profilN2=["±","⊆","∪","∩","∂","⊇","¾","∀","∇","∑","≈",""]
profilN3=["α","β","Ψ","φ","δ","ε","ζ","ξ","π","∑","σ","ω"]

if comEtablie == True:
if ser1.inWaiting() != 0 :
"""
valrecue = ser1.readline() # Lecture de 10 octets max dans le buffer de reception
# Valrecue = valrecue.decode('ascii')
E1.delete(0, END)
E1.insert(END,valrecue)
"""
valrecue = ser1.readline() # Lecture de 10 octets max dans le buffer de reception
Valrecue = valrecue.decode('ascii').encode('utf-8')
indice=int(Valrecue)-1
caractere=profilN1[indice]
#print codecs.decode(caractere,"utf-8")
textW.insert(END,profilN1[indice])
else:
pass
else:
pass
fen1.after(500,recevoir) # Mise à jour toutes les 500 ms
```


# *Graphic part*

```python
#-------------------------------------------------------#
#                    Code Graphique                     #
#-------------------------------------------------------#

	
# Le programme principal
fen1 = Tk() # Création de la fenêtre principale
fen1.title("Fenêtre Graphique du clavier bluetooth") # Titre ecrit dans la fenetre
fen1.config(bg='#ffffff') # Couleur de fond
fen1.geometry("400x200+400+100") # Dimension fenêtre (largeur x hauteur et postion X + Y)
fen1.resizable(width=True, height=True)  # Fenêtre non redimensionnable
#fenetre.maxsize(width=500, height=200)

#Déclaration des différents widgets
font1 = tkFont.Font(size=50, family='courier', weight='bold')
textW=Text(fen1, height=200, width= 250, wrap=NONE)
sy = Scrollbar(fen1, orient=VERTICAL, command = textW.yview)
sx = Scrollbar(fen1, orient=HORIZONTAL, command = textW.xview)
textW.config(yscrollcommand = sy.set, xscrollcommand = sx.set, font=font1)

#Placement du widget Text et des Scrollbar associés
sy.pack(side=RIGHT, fill=Y)
sx.pack(side=BOTTOM, fill=X)
textW.pack(side=RIGHT, fill=Y)

#Barre de menu
mainMenu = Menu(fen1)
#Ajout de la barre de menu a la fenêtre
fen1.config(menu = mainMenu) 

#création des menu fils
menuExample = Menu(mainMenu, tearoff=0)  #Menu fils
menuExample.add_command(label="New file", command=NewFile)  #Ajout d'une option au menu fils menuExample
menuExample.add_command(label="Open", command=Open)
menuExample.add_command(label="Save", command=Save)
menuExample.add_command(label="Save as", command=Save)

menuExample.add_separator()
menuExample.add_command(label="Quitter", command=fen1.destroy) 

menuConfiguration = Menu(mainMenu) #Menu fils
menuConfiguration.add_command(label="Profil 1", command=lambda :configuration("1")) #appel de la fonction configuration avec profil="1"
menuConfiguration.add_command(label="Profil 2", command=lambda :configuration("2"))
menuConfiguration.add_command(label="Profil 3", command=lambda :configuration("3"))
menuConfiguration.add_command(label="Profil 4", command=lambda :configuration("4"))

menuBluetooth = Menu(mainMenu)
menuBluetooth.add_command(label="Connexion", command=connecter)
menuBluetooth.add_command(label="Déconnexion", command=deconnecter)


menuHelp = Menu(mainMenu) #Menu fils
menuHelp.add_command(label="A propos", command=about)


#Ajout des menus fils a la barre de menus
mainMenu.add_cascade(label = "File", menu=menuExample)
mainMenu.add_cascade(label = "Configuration clavier", menu=menuConfiguration)
mainMenu.add_cascade(label = "Bluetooth", menu=menuBluetooth)
mainMenu.add_cascade(label = "Aide", menu=menuHelp)

recevoir()  # La fonction qui recupere les donnees presentes en reception RXD

fen1.mainloop() # affiche la fenêtre et lance la scrutation des évenements 
```