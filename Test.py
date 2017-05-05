import unittest
from Grille import *

class TestJeu(unittest.TestCase):

    def modulo(self):
        for i in range(9):
            print(i)
            print(i%3)

        return True

    def test_main(self):
        self.assertEqual(true,self.modulo())
    
  #  def test_grilleGeneration(self):

 #       #self.assertEqual(True,self.modulo())
 #       grille = Grille(10,10)
 #       self.assertEqual("Error Out Of Bound",grille.get_Case(40,1))
 #       self.assertEqual(4,grille.get_Case(1,1))

#    def test_grilleInitialisation(self):
#        grille = Grille(10,10)

  #      for i in range(grille.get_longueur()):
  #          for j in range(grille.get_largeur()):
  #              self.assertEqual(1,grille.get_Case(i,j)%3)
unittest.main()
