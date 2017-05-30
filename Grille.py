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
        random.seed(9876543210) #Seed fixed for test purpose
        for i in range(x):
            rows = {}
            for j in range(y):

                #toto = random.getstate()
                #print(toto)
                rows[j]=random.choice([CONST_TERRE,CONST_EAU,CONST_MONTAGNE])
            #print(rows)
            self._grille[i]=rows

    def get_Case(self,x,y):
        try:
            return self._grille[x][y]
        except KeyError:
            return "Error Out Of Bound"

    def get_grille(self):
        return self._grille
    def set_case(self,x,y,value):
        self._grille[x][y] = value
    def get_largeur(self):
        return self._largeur

    def get_longueur(self):
        return self._longueur
