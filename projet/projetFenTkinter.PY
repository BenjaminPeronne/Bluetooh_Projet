
#!/usr/bin/Python
# -*- coding: cp1252 -*-

"""
  fenêtre graphique Tkinter 
"""


# Fichier : projetFenTkinter.py
# Auteur : GEFFREY

# Importation des modules (packages)
from Tkinter import * # On importe Tkinter
import tkMessageBox, tkFileDialog 
# Declaration des variables globales
chemin_fichier=None

# Les fonctions de l'application
def quitter():
    """
    La fonction qui termine l'application graphique
    """
    fen1.destroy() #Destruction et fermeture de la fenetre

def connexion():
    """permet d'afficher a à l'écran un message d'information dans une fenêtre"""
    tkMessageBox.showinfo("Connexion Bluetooth", "Conected")


def deconnexion():
    """permet d'afficher a à l'écran un message d'information dans une fenêtre"""
    tkMessageBox.showinfo("Déconnexion Bluetooth", "Disconected")


def NewFile():
    """permet d'afficher a à l'écran un message d'information sur une ouvelle  fenêtre"""
    tkMessageBox.showinfo("New File")
	
def about():
    """permet d'afficher a à l'écran un message d'information dans une fenêtre"""
    tkMessageBox.showinfo("A propos", "Version 1.0")
	
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
    """permet d'accéder au profil demander celon l'odre reçu"""
    tkMessageBox.showwarning(profil)

def Save():
    global chemin_fichier
    contenu=textW.get("1.0",END)
    print contenu
    mon_fichier = open(chemin_fichier, "w")
    mon_fichier.write(contenu) 
    mon_fichier.close()


# Le programme principal
#########################################################
# Création de la fenêtre principale                     #
#########################################################  
fen1 = Tk() # Création de la fenêtre principale
fen1.title("Fenetre graphique Tkinter ") # Titre ecrit dans la fenetre
fen1.config(bg='#ffffff') # Couleur de fond
fen1.geometry("400x200+400+100") # Dimension fenêtre (largeur x hauteur et postion X + Y)
fen1.resizable(width=True, height=True)  # Fenêtre non redimensionnable
#fenetre.maxsize(width=500, height=200)

#Déclaration des différents widgets
textW=Text(fen1, height=200, width= 250, wrap=NONE)
sy = Scrollbar(fen1, orient=VERTICAL, command = textW.yview)
sx = Scrollbar(fen1, orient=HORIZONTAL, command = textW.xview)
textW.config(yscrollcommand = sy.set, xscrollcommand = sx.set)

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
menuExample.add_command(label="Connexion", command=connexion)
menuExample.add_command(label="Déconnexion", command=deconnexion)
menuExample.add_command(label="Open", command=Open)
menuExample.add_command(label="Save", command=Save)
menuExample.add_command(label="Save as", command=Save)

menuExample.add_separator()
menuExample.add_command(label="Quitter", command=fen1.destroy) 

menuConfiguration = Menu(mainMenu) #Menu fils
menuConfiguration.add_command(label="Profil 1", command=lambda :Configuration("1")) #appel de la fonction configuration avec profil="1"
menuConfiguration.add_command(label="Profil 2", command=lambda :Configuration("2"))
menuConfiguration.add_command(label="Profil 3", command=lambda :Configuration("3"))
menuConfiguration.add_command(label="Profil 4", command=lambda :Configuration("4"))

menuHelp = Menu(mainMenu) #Menu fils
menuHelp.add_command(label="A propos", command=about)


#Ajout des menus fils a la barre de menus
mainMenu.add_cascade(label = "File", menu=menuExample)
mainMenu.add_cascade(label = "Configuration clavier", menu=menuConfiguration)
mainMenu.add_cascade(label = "Aide", menu=menuHelp)

fen1.mainloop() # affiche la fenêtre et lance la scrutation des événements 

