import random
CONST_TERRE = 1
CONST_EAU = 4
CONST_MONTAGNE = 7
CONST_MORT = 1
CONST_VIVANT = 2
CONST_ZOMBIE = 3

class Grille:

    def __init__(self,x,y):
        self._grille = {}
        self._largeur = y
        self._longueur = x
        random.seed(9876543210)
        for i in range(x):
            rows = {}
            for j in range(y):

                #toto = random.getstate()
                #print(toto)
                rows[j]=random.choice([CONST_TERRE,CONST_EAU,CONST_MONTAGNE])
            self._grille[i]=rows

    def check_voisins(self,x,y):
        nb_Mort = 0
        nb_Zombie = 0
        nb_Vivant = 0
        for i in range(-1,2):
            for j in range(-1,2):
                if i != 0 and j !=0:
                    print("i")
                    print(i)
                    print("j")
                    print(j)
                    print("status")
                    print(self._grille[x+i][y+j])
                    if self._grille[x+i][y+j] in {2,5,8}:
                        nb_Vivant+=1
                    elif self._grille[x+i][y+j] in {3,6,9}:
                        nb_Zombie+=1
                    elif self._grille[x+i][y+j] in {1,4,7}:
                        nb_Mort+=1
        return nb_Mort,nb_Zombie,nb_Vivant


    def get_Case(self,x,y):
        try:
            return self._grille[x][y]
        except KeyError:
            return "Error Out Of Bound"

    def get_grille(self):
        return self._grille
    def get_largeur(self):
        return self._largeur

    def get_longueur(self):
        return self._longueur

#grille = Grille (10,10)
#mort,zombie,vivant = grille.check_voisins(5,5)
#print("mort")
#print(mort)
#print("vivant")
#print(vivant)
#print("zombie")
#print(zombie)
