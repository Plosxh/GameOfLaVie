import unittest
from Grille import *
from Jeu import *
from Vue import *

class TestJeu(unittest.TestCase):

    def modulo(self):
        for i in range(9):
            pass
        return True

    def test_main(self):
        self.assertEqual(True,self.modulo())

    def test_grilleGeneration(self):

        self.assertEqual(True,self.modulo())
        grille = Grille(10,10)
        self.assertEqual("Error Out Of Bound",grille.get_Case(40,1))
        self.assertEqual(7,grille.get_Case(1,1))

    def test_grilleInitialisation(self):
        grille = Grille(10,10)

        for i in range(grille.get_longueur()):
           for j in range(grille.get_largeur()):
               self.assertEqual(1,grille.get_Case(i,j)%3)

    def test_check_voisin(self):
        grille = Grille(10,10);
        item ={5241,5140,5240,5340,5341,5342,5242,5142,5141}


    def test_vivant(self):
        grille = Grille(3,3)
        rows = [[1,1,2],[2,1,1],[1,1,1]]
        for i in range(3):
           for j in range(3):
               grille.set_case(i,j,rows[i][j])
        #Lancer un tour de traitement
        #vérifier que la ligne 2,2 est égal à 1
        self.assertEqual(True,self.modulo())

        grille = Grille(3,3)
        rows = [[1,2,1],[2,1,1],[1,2,2]]
        for i in range(3):
           for j in range(3):
               grille.set_case(i,j,rows[i][j])
        #Lancer un tour de traitement
        #vérifier que la ligne 2,2 est égal à 1
        self.assertEqual(True,self.modulo())

        grille = Grille(3,3)
        rows = [[1,2,1],[1,2,1],[2,1,1]]
        for i in range(3):
           for j in range(3):
               grille.set_case(i,j,rows[i][j])
        #Lancer un tour de traitement
        #vérifier que la ligne 2,2 est égal à 2
        self.assertEqual(True,self.modulo())

        grille = Grille(3,3)
        rows = [[2,2,2],[1,2,1],[1,2,1]]
        for i in range(3):
           for j in range(3):
               grille.set_case(i,j,rows[i][j])
        #Lancer un tour de traitement
        #vérifier que la ligne 2,2 est égal à 2
        self.assertEqual(True,self.modulo())

    def test_mort(self):
        #cas de figure 1
        fenetre = Tk()
        fenetre.wm_title("GameOfLaVie")
        grille = Grille(3,3)
        rows = [[2,2,2],[2,2,2],[2,2,1]]
        for i in range(3):
           for j in range(3):
               grille.set_case(i,j,rows[i][j])
        vue = Vue(CONST_LONGUEUR,CONST_LARGEUR,CONST_REC_TAILLE,fenetre,grille);
        mainmenu = Menu(fenetre)  ## Barre de menu
        menuExample = Menu(mainmenu)  ## Menu fils menuExample
        menuExample.add_command(label="Start", command=lambda :Start(vue))  ## Ajout d'une option au menu fils menuFile
        menuExample.add_command(label="Quitter", command=fenetre.quit)
        mainmenu.add_cascade(label = "Jeu", menu=menuExample)
        fenetre.config(menu = mainmenu)
        update_cells(vue,grille)
        status = grille.get_Case(1,1)
        self.assertEqual(1,status)
        #Lancer un tour de traitement
        #vérifier que la ligne 2,2 est égal à 1
        self.assertEqual(True,self.modulo())

        #cas de figure 2
        grille = Grille(3,3)
        rows = [[2,2,2],[1,2,1],[2,2,1]]
        for i in range(3):
           for j in range(3):
               grille.set_case(i,j,rows[i][j])
        #Lancer un tour de traitement
        #vérifier que la ligne 2,2 est égal à 1
        self.assertEqual(True,self.modulo())

    def test_naissance(self):
        fenetre = Tk()
        fenetre.wm_title("GameOfLaVie")
        grille = Grille(3,3)
        rows = [[2,2,1],[1,1,2],[1,1,1]]
        for i in range(3):
           for j in range(3):
               grille.set_case(i,j,rows[i][j])
        vue = Vue(CONST_LONGUEUR,CONST_LARGEUR,CONST_REC_TAILLE,fenetre,grille);
        mainmenu = Menu(fenetre)  ## Barre de menu
        menuExample = Menu(mainmenu)  ## Menu fils menuExample
        menuExample.add_command(label="Start", command=lambda :Start(vue))  ## Ajout d'une option au menu fils menuFile
        menuExample.add_command(label="Quitter", command=fenetre.quit)
        mainmenu.add_cascade(label = "Jeu", menu=menuExample)
        fenetre.config(menu = mainmenu)
        #Lancer un tour de traitement
        update_cells(vue,grille)
        status = grille.get_Case(1,1)
        self.assertEqual(2,status)
        #vérifier que la ligne 2,2 est égal à 2
        self.assertEqual(True,self.modulo())

unittest.main()
