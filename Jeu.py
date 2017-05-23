from tkinter import *
from Grille import *
CONST_REC_TAILLE = 5
CONST_LONGUEUR = 500
CONST_LARGEUR = 500
fenetre = Tk()
fenetre.wm_title("GameOfLaVie")

#label = Label(fenetre, text="Hello World")
#label.pack()
grille = Grille(int(CONST_LARGEUR/CONST_REC_TAILLE),int(CONST_LONGUEUR/CONST_REC_TAILLE))
canvas = Canvas(fenetre, width=CONST_LONGUEUR, height=CONST_LARGEUR, background='white')
def clicked(event, arg):
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
    update_cell();
    for value in range(len(rec)):
        if rec[value] == "zombie":
            #print("RUN !")
            check_voisin(item,coords)

    return coords

def update_cell():
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
    pass;

mainmenu = Menu(fenetre)  ## Barre de menu
menuExample = Menu(mainmenu)  ## Menu fils menuExample
menuExample.add_command(label="Start", command=Start)  ## Ajout d'une option au menu fils menuFile
menuExample.add_command(label="Quitter", command=fenetre.quit)


mainmenu.add_cascade(label = "Jeu", menu=menuExample)

fenetre.config(menu = mainmenu)

i = 0
for x in range(int(CONST_LARGEUR/CONST_REC_TAILLE)):
    for y in range(int(CONST_LONGUEUR/CONST_REC_TAILLE)):
        i+=1
        rect_tags = {}
        color = "black"
        #rect_tags=""
        #print(grille.get_grille())
        grille_status = grille.get_Case(x,y)
        grille_stipple = "gray25"
        #print(grille_status)
        if grille_status ==1:
            rect_tags="terre"+","+str(i)
            color="green"
            if i%3 == 0:
                grille_stipple = "gray50"
        elif grille_status ==4:
            rect_tags="eau"+","+str(i)
            color="blue"
            if i%3 == 0:
                grille_stipple = "gray75"
        elif grille_status ==7:
            pass
            rect_tags="montagne"+","+str(i)
            color="brown"
        #rec = canvas.create_rectangle(x*CONST_REC_TAILLE,y*CONST_REC_TAILLE,(x+1)*CONST_REC_TAILLE,(y+1)*CONST_REC_TAILLE,fill=color,outline="black",tags=rect_tags,stipple=grille_stipple)
        rec = canvas.create_rectangle(x*CONST_REC_TAILLE,y*CONST_REC_TAILLE,(x+1)*CONST_REC_TAILLE,(y+1)*CONST_REC_TAILLE,fill=color,outline="black",tags=rect_tags)
        monrec = canvas.find_withtag(rect_tags[0])
        data={"tag": rect_tags}
        canvas.tag_bind(rect_tags,"<Button-1>",lambda event, arg=data: clicked(event, arg))

canvas.pack()

fenetre.mainloop()
