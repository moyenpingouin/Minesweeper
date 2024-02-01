def voisins(coordonnees:tuple(),tableau:list[list]):
    """fonction qui donne les coordonnées des voisins"""
    x=coordonnees[0]
    y=coordonnees[1]
    hauteur=len(tableau)
    longueur=len(tableau[0])
    liste=[]
    for i in range(x-1, x+2):
        for j in range(y-1, y+2):
            liste.append((i,j))
    liste2=list(liste)
    #supprime les coordonnées hors du tableau + point en question
    for i in liste:
        if i[0]<0 or i[1]<0 or (i[0]==x and i[1]==y) or (i[0]>longueur or i[1]>hauteur):
            liste2.remove(i)
    return liste2

class case:
    def __init__(self,est_bombe:bool, coordonnees:tuple, tableau:list[list]):
        self.est_bombe=est_bombe
        self.voisins= [tableau[i[1]][i[0]] for i in voisins(coordonnees,tableau)]
        if not self.est_bombe:
            nb=0
            for i in self.voisins:
                if (tableau[i[1]][i[0]]).bombe():
                    nb+=1
            self.etat=str(nb)
        else:
            self.etat='Bombe'


    def vide(self):
        return self.nb==0

    def bombe(self):
        return self.est_bombe

    def __str__(self) -> str:
        return self.etat
    
a=case(True,(1,6),[[1,2,3,4,5,6,7],
                   [1,2,3,4,5,6,7],
                   [1,2,3,4,5,6,7]])


print(voisins((1,6),[[1,2,3,4,5,6,7],
                   [1,2,3,4,5,6,7],
                   [1,2,3,4,5,6,7]]))