from tkinter import *

class Vue:
    def __init__(self,longueur,larg,rec_taille,fenetre,grille):


        self.canvas = Canvas(fenetre, width=longueur, height=larg, background='white')

        i = 0
        for x in range(grille.get_largeur()):
            for y in range(grille.get_longueur()):
                i+=1
                rect_tags = {}
                color = "black"
                grille_status = grille.get_Case(y,x)
                if grille_status ==1:
                    rect_tags="terre"+","+str(i)
                    color="green"
                elif grille_status ==4:
                    rect_tags="eau"+","+str(i)
                    color="blue"
                elif grille_status ==7:
                    rect_tags="montagne"+","+str(i)
                    color="brown"
                elif grille_status in {2,5,8}:
                    pass
                    rect_tags="vivant"+","+str(i)
                    color="black"
                elif grille_status in {3,6,9}:
                    pass
                    rect_tags="zombie"+","+str(i)
                    color="white"
                #rec = canvas.create_rectangle(x*CONST_REC_TAILLE,y*CONST_REC_TAILLE,(x+1)*CONST_REC_TAILLE,(y+1)*CONST_REC_TAILLE,fill=color,outline="black",tags=rect_tags,stipple=grille_stipple)
                rec = self.canvas.create_rectangle(x*rec_taille,y*rec_taille,(x+1)*rec_taille,(y+1)*rec_taille,fill=color,outline="black",tags=rect_tags)
                monrec = self.canvas.find_withtag(rect_tags[0])
                data={"tag": rect_tags}
                self.canvas.tag_bind(rect_tags,"<Button-1>",lambda event, arg=data: self.clicked(event, arg, grille, rec_taille))

        self.canvas.pack()

    def clicked(self,event, arg, grille,rec_taille):
        coords = self.canvas.coords(arg["tag"])
        item = self.canvas.find_withtag(arg["tag"])
        self.canvas.addtag_withtag("vivant", arg["tag"])
        self.canvas.itemconfig(arg["tag"], fill="yellow")
        cell_ligne = int(coords[0]/rec_taille)
        cell_colonne = int(coords[1]/rec_taille)
        new_val = 1
        if grille.get_Case(cell_colonne,cell_ligne)==1:
            new_val = 2
        elif grille.get_Case(cell_colonne,cell_ligne) ==4:
            new_val = 5
        elif grille.get_Case(cell_colonne,cell_ligne) == 7:
            new_val = 8
        grille.set_case(cell_colonne,cell_ligne,new_val)

        return coords

    def update_vue(self,x,y,rec_taille,grille):
        #print("to status : "+status)
        '''
            item = self.canvas.find_closest((x*rec_taille),y*rec_taille)
            if status == "v":
                self.canvas.itemconfig(item, fill="yellow")
            elif status == "z":
                self.canvas.itemconfig(item, fill="black")
        '''
        for i in range(len(grille.get_grille())):
            for j in range(len(grille.get_grille()[i])):
                item = self.canvas.find_closest((i*rec_taille-2),j*rec_taille-2)
                if grille.get_Case(i,j) == "1":
                    self.canvas.itemconfig(item, fill="green")
                elif grille.get_Case(i,j) == "2":
                    self.canvas.itemconfig(item, fill="blue")
                elif grille.get_Case(i,j) == "3":
                    self.canvas.itemconfig(item, fill="brown")
                elif grille.get_Case(i,j) in {2,5,8}:
                    #print("i : "+str(i)+" j : "+str(j))
                    #print(grille.get_Case(i,j))
                    self.canvas.itemconfig(item, fill="yellow")
                elif grille.get_Case(i,j) in {3,6,9}:
                    self.canvas.itemconfig(item, fill="black")
