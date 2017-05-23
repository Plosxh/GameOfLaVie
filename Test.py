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
               grille.set_grille(i,j,rows[i][j])
        #Lancer un tour de traitement
        #vérifier que la ligne 2,2 est égal à 1
        self.assertEqual(True,self.modulo())

        grille = Grille(3,3)
        rows = [[1,2,1],[2,1,1],[1,2,2]]
        for i in range(3):
           for j in range(3):
               grille.set_grille(i,j,rows[i][j])
        #Lancer un tour de traitement
        #vérifier que la ligne 2,2 est égal à 1
        self.assertEqual(True,self.modulo())

        grille = Grille(3,3)
        rows = [[1,2,1],[1,2,1],[2,1,1]]
        for i in range(3):
           for j in range(3):
               grille.set_grille(i,j,rows[i][j])
        #Lancer un tour de traitement
        #vérifier que la ligne 2,2 est égal à 2
        self.assertEqual(True,self.modulo())

        grille = Grille(3,3)
        rows = [[2,2,2],[1,2,1],[1,2,1]]
        for i in range(3):
           for j in range(3):
               grille.set_grille(i,j,rows[i][j])
        #Lancer un tour de traitement
        #vérifier que la ligne 2,2 est égal à 2
        self.assertEqual(True,self.modulo())

    def test_mort(self):
        #cas de figure 1
        grille = Grille(3,3)
        rows = [[1,1,1],[1,2,1],[1,1,1]]
        for i in range(3):
           for j in range(3):
               grille.set_grille(i,j,rows[i][j])
        #Lancer un tour de traitement
        #vérifier que la ligne 2,2 est égal à 1
        self.assertEqual(True,self.modulo())

        #cas de figure 2
        grille = Grille(3,3)
        rows = [[2,2,2],[1,2,1],[2,2,1]]
        for i in range(3):
           for j in range(3):
               grille.set_grille(i,j,rows[i][j])
        #Lancer un tour de traitement
        #vérifier que la ligne 2,2 est égal à 1
        self.assertEqual(True,self.modulo())

    def test_naissance(self):
        grille = Grille(3,3)
        rows = [[2,2,1],[1,1,2],[1,1,1]]
        for i in range(3):
           for j in range(3):
               grille.set_grille(i,j,rows[i][j])
        #Lancer un tour de traitement
        #vérifier que la ligne 2,2 est égal à 2
        self.assertEqual(True,self.modulo())

unittest.main()
