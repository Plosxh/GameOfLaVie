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

    canvas.addtag_withtag("zombie", arg["tag"])
    canvas.itemconfig(arg["tag"], fill="yellow")

    #rec = canvas.find_withtag(arg["tag"])
    rec = canvas.gettags(arg["tag"])
    for value in range(len(rec)):
        if rec[value] == "zombie":
            #print("RUN !")
            check_voisin(coords)

    return coords

def check_voisin(coords):
    rec = canvas.find_overlapping(coords[0], coords[1], coords[2], coords[3])
    #print(coords)
    #print(len(rec))
    for i in range(len(rec)):
        rdm = random.randint(0,1000)
        print(rdm)
        if rdm > 999:
            canvas.itemconfig(rec[i], fill="yellow")

i = 0
for x in range(int(CONST_LARGEUR/CONST_REC_TAILLE)):
    for y in range(int(CONST_LONGUEUR/CONST_REC_TAILLE)):
        i+=1
        rect_tags = {}
        color = "black"
        rect_tags=""
        #print(grille.get_grille())
        grille_status = grille.get_Case(x,y)
        grille_stipple = "gray25"
        #print(grille_status)
        if grille_status ==1:
            rect_tags="terre"+str(i)
            color="green"
            if i%3 == 0:
                grille_stipple = "gray50"
        elif grille_status ==4:
            rect_tags="eau"+str(i)
            color="blue"
            if i%3 == 0:
                grille_stipple = "gray75"
        elif grille_status ==7:
            pass
            rect_tags="montagne"+str(i)
            color="brown"
        #rec = canvas.create_rectangle(x*CONST_REC_TAILLE,y*CONST_REC_TAILLE,(x+1)*CONST_REC_TAILLE,(y+1)*CONST_REC_TAILLE,fill=color,outline="black",tags=rect_tags,stipple=grille_stipple)
        rec = canvas.create_rectangle(x*CONST_REC_TAILLE,y*CONST_REC_TAILLE,(x+1)*CONST_REC_TAILLE,(y+1)*CONST_REC_TAILLE,fill=color,outline="black",tags=rect_tags)
        monrec = canvas.find_withtag(rect_tags[0])
        data={"tag": rect_tags}
        canvas.tag_bind(rect_tags,"<Button-1>",lambda event, arg=data: clicked(event, arg))

canvas.pack()

fenetre.mainloop()
