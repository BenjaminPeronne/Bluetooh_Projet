#-*- coding:Utf-8 -*-
# -*- coding: cp1252 -*-


# File : rfcomm-server.py
# Auth : Benjamin Peronne
# Fichier : fenMenu.py


#   Importation des modules (packages)       #
from Tkinter import*
import tkMessageBox 
from bluetooth import*

server_sock=BluetoothSocket( RFCOMM ) #définit le service de communication


#-------------------------------------------------------#
#                    Code Application                   #
#-------------------------------------------------------#

# Les fonctions de l'application
def connexion():
    """permet d'afficher a à l'écran un message d'information dans une fenêtre"""
    tkMessageBox.showinfo("Connexion Bluetooth", "Conected")


def deconnexion():
    """permet d'afficher a à l'écran un message d'information dans une fenêtre"""
    tkMessageBox.showinfo("Déconnexion Bluetooth", "Disconected")

def about():
    """permet d'afficher a à l'écran un message d'information dans une fenêtre"""
    tkMessageBox.showinfo("A propos", "Version 1.0")
	
    
def warning():
    """permet d'afficher a à l'écran un message de type warning dans une fenêtre"""
    tkMessageBox.showwarning("Warning", "Attention à vous ...")

	
# Le programme principal
fen1=Tk() #création de la fenêtre principale

#Déclaration des différents widgets
textW=Text(fen1, height=20, width= 50, wrap=NONE)
sy = Scrollbar(fen1, orient=VERTICAL, command = textW.yview)
sx = Scrollbar(fen1, orient=HORIZONTAL, command = textW.xview)
textW.config(yscrollcommand = sy.set, xscrollcommand = sx.set) 

#Placement du widget Text et des Scrollbar associés
sy.pack(side=RIGHT, fill=Y)
sx.pack(side=BOTTOM, fill=X)
textW.pack(side=RIGHT, fill=Y)

mainMenu = Menu(fen1)  #Barre de menu

menuExample = Menu(mainMenu, tearoff=0)  #Menu fils
menuExample.add_command(label="Connexion", command=connexion)  #Ajout d'une option au menu fils menuExample
menuExample.add_command(label="Déconnexion", command=deconnexion)

menuWarning = Menu(mainMenu) #Menu fils
menuWarning.add_command(label="Warning", command=warning)

menuHelp = Menu(mainMenu) #Menu fils
menuHelp.add_command(label="A propos", command=about)

#Ajout des menus fils a la barre de menus
mainMenu.add_cascade(label = "Bluetooth", menu=menuExample)
mainMenu.add_cascade(label = "warning", menu=menuWarning)
mainMenu.add_cascade(label = "Aide", menu=menuHelp)
mainMenu.add_cascade(label = "Quitter", command=fen1.destroy)
  
#Ajout de la barre de menu a la fenêtre
fen1.config(menu = mainMenu) 

fen1.mainloop()
