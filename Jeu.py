from tkinter import *
from Grille import *
from Vue import *

CONST_REC_TAILLE = 50
CONST_LONGUEUR = 500
CONST_LARGEUR = 500

def main():
    fenetre = Tk()
    fenetre.wm_title("GameOfLaVie")
    grille = Grille(int(CONST_LARGEUR/CONST_REC_TAILLE),int(CONST_LONGUEUR/CONST_REC_TAILLE))
    vue = Vue(CONST_LONGUEUR,CONST_LARGEUR,CONST_REC_TAILLE,fenetre,grille);
    mainmenu = Menu(fenetre)  ## Barre de menu
    menuExample = Menu(mainmenu)  ## Menu fils menuExample
    menuExample.add_command(label="Start", command=Start)  ## Ajout d'une option au menu fils menuFile
    menuExample.add_command(label="Quitter", command=fenetre.quit)
    mainmenu.add_cascade(label = "Jeu", menu=menuExample)
    fenetre.config(menu = mainmenu)
    fenetre.mainloop()

#label = Label(fenetre, text="Hello World")
#label.pack()
#grille = Grille(int(CONST_LARGEUR/CONST_REC_TAILLE),int(CONST_LONGUEUR/CONST_REC_TAILLE))
#canvas = Canvas(fenetre, width=CONST_LONGUEUR, height=CONST_LARGEUR, background='white')
def clicked(event, arg):
    print("in the Jeu")
    coords = canvas.coords(arg["tag"])
    item = canvas.find_withtag(arg["tag"])
    #print(arg["tag"])
    canvas.addtag_withtag("vivant", arg["tag"])
    canvas.itemconfig(arg["tag"], fill="yellow")
    #print(arg["tag"])
    #rec = canvas.find_withtag(arg["tag"])
    check_voisin(item,coords)
    rec = canvas.gettags(arg["tag"])
    #print(len(rec))
    update_cells();
    for value in range(len(rec)):
        if rec[value] == "zombie":
            #print("RUN !")
            check_voisin(item,coords)

    return coords

def update_cells():
    cells = canvas.find_withtag("all");
    for cell in cells:
        cell_coords = canvas.coords(cell);
        #check_voisin(cell,cell_coords);
        #print(cell_coords);
    print("END UPDATE")

def check_voisin(item,coords):
    print(item[0])
    #rec = canvas.find_overlapping(coords[0], coords[1], coords[2], coords[3])
    rec = canvas.find_enclosed(coords[0]-(CONST_REC_TAILLE+1),coords[1]-(CONST_REC_TAILLE+1),coords[2]+(CONST_REC_TAILLE+1),coords[3]+(CONST_REC_TAILLE+1))
    print("coords modif")
    print(rec)
    for r in rec:
        #if r != item[0]:
        #    item_tag = canvas.gettags(r)
        item_tags = canvas.gettags(r)
        for tag in item_tags:
            if tag == "vivant":
                print(str(r)+" IS ALIVE !")
    #Rec contient les case adjacentes à la case donnée en param
    #for i in range(len(rec)):
        #print(rec[i])
        #Choisit un nombre random pour le faire ou non devenir zombie

        #canvas.itemconfig(rec[i], fill="yellow")

def turnToZombie():
    rdm = random.randint(0,1000)
    if rdm > 999:
        return True;
    else:
        return False;
def Start():
    print("start")
    update_cells();
