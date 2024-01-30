def voisins(coordonnees):
    x=coordonnees[0]
    y=coordonnees[1]
    liste=[]
    for i in range(x-1, x+2):
        for j in range(y-1, y+2):
            liste.append((i,j))
    liste2=list(liste)
    for i in liste:
        if i[0]<0 or i[1]<0 or (i[0]==x and i[1]==y):
            liste2.remove(i)
    return liste2

class case:
    def __init__(self,est_bombe, coordonnees, tableau):
        self.est_bombe=est_bombe
        self.voisins= voisins(coordonnees)

        if not self.est_bombe:
            nb=0
            for i in self.voisins:
                if (tableau[i[1]][i[0]]).bombe():
                    nb+=1
            self.nb=nb


    def vide(self):
        return self.nb==0

    def bombe(self):
        return self.est_bombe



