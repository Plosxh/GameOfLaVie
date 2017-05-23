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


unittest.main()
