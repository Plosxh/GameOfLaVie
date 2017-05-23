from tkinter import *

class Vue:
    def __init__(self,longueur,larg,rec_taille,fenetre,grille):


        self.canvas = Canvas(fenetre, width=longueur, height=larg, background='white')

        i = 0
        for x in range(int(larg/rec_taille)):
            for y in range(int(longueur/rec_taille)):
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
                elif grille_status in {2,5,8}:
                    pass
                    rect_tags="vivant"+","+str(i)
                    color="brown"
                elif grille_status in {3,6,9}:
                    pass
                    rect_tags="zombie"+","+str(i)
                    color="brown"
                #rec = canvas.create_rectangle(x*CONST_REC_TAILLE,y*CONST_REC_TAILLE,(x+1)*CONST_REC_TAILLE,(y+1)*CONST_REC_TAILLE,fill=color,outline="black",tags=rect_tags,stipple=grille_stipple)
                rec = self.canvas.create_rectangle(x*rec_taille,y*rec_taille,(x+1)*rec_taille,(y+1)*rec_taille,fill=color,outline="black",tags=rect_tags)
                monrec = self.canvas.find_withtag(rect_tags[0])
                data={"tag": rect_tags}
                self.canvas.tag_bind(rect_tags,"<Button-1>",lambda event, arg=data: self.clicked(event, arg))

        self.canvas.pack()

    def clicked(self,event, arg):
        coords = self.canvas.coords(arg["tag"])
        item = self.canvas.find_withtag(arg["tag"])
        self.canvas.addtag_withtag("vivant", arg["tag"])
        self.canvas.itemconfig(arg["tag"], fill="yellow")
        #for value in range(len(rec)):
        #    if rec[value] == "zombie":
        #        #print("RUN !")
        #        check_voisin(item,coords)

        return coords
