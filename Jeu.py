from tkinter import *
from Grille import *
from Vue import *

CONST_REC_TAILLE = 50
CONST_LONGUEUR = 500
CONST_LARGEUR = 500

def update_cells(vue,grille):
    la_grille = grille.get_grille()
    update_grille = grille
    #print(la_grille)
    for i in range(len(la_grille)):
        for j in range(len(la_grille[i])):
            vi = check_voisin(grille,i,j)
            cell_status = grille.get_Case(i,j)
            if cell_status in {1,4,7}:
                #Cell is dead
                if vi == 3:
                    #New cell is born
                    update_grille.set_case(i,j,cell_status+1)
                if vi == 2:
                    #nothing happen
                    pass
            elif cell_status in {2,5,8}:
                #cell is alive
                if vi>4:
                    if turnToZombie():
                        #turned into a zombi
                        update_grille.set_case(i,j,cell_status+2)
                    else:
                        #Died
                        update_grille.set_case(i,j,cell_status-1)
            elif cell_status in {3,6,9}:
                pass
                #cell is zombie, and can't be reanimate of killed
            else:
                #aucun des cas n'est bon
                pass
    vue.update_vue(i,j,CONST_REC_TAILLE,update_grille)
    #print("END UPDATE")
    return update_grille

def check_voisin(la_grille,x,y):
    delta_x =1
    delta_y = 1
    nb_zombie =0
    nb_vivant = 0
    nb_mort = 0
    x_max = la_grille.get_largeur()
    y_max = la_grille.get_longueur()
    #print("x : "+str(x)+" y :  "+str(y))
    if la_grille.get_Case(x,y-delta_y) in {2,5,8} and y != 0:
        #à gauche est vivante
        nb_vivant+=1
    elif la_grille.get_Case(x,y-delta_y) in {1,4,7} and y != 0:
        #à gauche est morte
        nb_mort+=1
    else:
        nb_zombie+=1
        #à gauche est zombie

    if la_grille.get_Case(x,y+delta_y) in {2,5,8} and y != y_max:
        #à droite est vivante
        nb_vivant+=1
    elif la_grille.get_Case(x,y+delta_y) in {1,4,7} and y != y_max:
        #à droite est morte
        nb_mort+=1
    else:
        #à droite est zombie
        nb_zombie+=1

    if la_grille.get_Case(x-delta_x,y) in {2,5,8} and x != 0:
        #en haut est vivante
        nb_vivant+=1
    elif la_grille.get_Case(x-delta_x,y) in {1,4,7} and x != 0:
        #en haut est morte
        nb_mort+=1
    else:
        #en haut est zombie
        nb_zombie+=1

    if la_grille.get_Case(x+delta_x,y) in {2,5,8} and x != x_max:
        #en bas est vivante
        nb_vivant+=1
    elif la_grille.get_Case(x+delta_x,y) in {1,4,7} and x != x_max:
        #en bas est morte
        nb_mort+=1
    else:
        #en bas est zombie
        nb_zombie+=1

    if la_grille.get_Case(x-delta_x,y-delta_y) in {2,5,8} and x != 0 and y != 0:
        #à gauche en haut est vivante
        nb_vivant+=1
    elif la_grille.get_Case(x-delta_x,y-delta_y) in {1,4,7} and x != 0 and y != 0:
        #à gauche en haut est morte
        nb_mort+=1
    else:
        #à gauche en haut est zombie
        nb_zombie+=1

    if la_grille.get_Case(x+delta_x,y-delta_y) in {2,5,8} and y != 0 and x != x_max:
        #à gauche en bas est vivante
        nb_vivant+=1
    elif la_grille.get_Case(x+delta_x,y-delta_y) in {1,4,7} and y != 0 and x != x_max:
        #à gauche en bas est morte
        nb_mort+=1
    else:
        #à gauche en bas est zombie
        nb_zombie+=1

    if la_grille.get_Case(x+delta_x,y+delta_y) in {2,5,8} and y != y_max and x != x_max:
        #à droite en bas est vivante
        nb_vivant+=1
    elif la_grille.get_Case(x+delta_x,y+delta_y) in {1,4,7} and y != y_max and x != x_max:
        #à droite en bas est morte
        nb_mort+=1
    else:
        #à droite en bas est zombie
        nb_zombie+=1

    if la_grille.get_Case(x-delta_x,y+delta_y) in {2,5,8} and x != 0 and y != y_max:
        #à droite en haut est vivante
        nb_vivant+=1
    elif la_grille.get_Case(x-delta_x,y+delta_y) in {1,4,7} and x != 0 and y != y_max:
        #à droite en haut est morte
        nb_mort+=1
    else:
        #à droite en haut est zombie
        nb_zombie+=1
    if nb_vivant == 8:
        pass
        #print("x = "+str(x)+" y = "+str(y))
    return nb_vivant


def turnToZombie():
    rdm = random.randint(0,1000)
    if rdm > 999:
        return True;
    else:
        return False;
def Start(vue):
    print("start")
    grille = update_cells(vue,grille);

def funcToto():
    print("toto")


if __name__ == "__main__":
    fenetre = Tk()
    fenetre.wm_title("GameOfLaVie")
    grille = Grille(int(CONST_LARGEUR/CONST_REC_TAILLE),int(CONST_LONGUEUR/CONST_REC_TAILLE))
    vue = Vue(CONST_LONGUEUR,CONST_LARGEUR,CONST_REC_TAILLE,fenetre,grille);
    mainmenu = Menu(fenetre)  ## Barre de menu
    menuExample = Menu(mainmenu)  ## Menu fils menuExample
    menuExample.add_command(label="Start", command=lambda :Start(vue))  ## Ajout d'une option au menu fils menuFile
    menuExample.add_command(label="Quitter", command=fenetre.quit)
    mainmenu.add_cascade(label = "Jeu", menu=menuExample)
    fenetre.config(menu = mainmenu)
    fenetre.mainloop()
