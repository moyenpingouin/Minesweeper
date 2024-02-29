def voisins(coordonnees:tuple(),tableau:list[list]):
    """fonction qui donne les coordonnées des voisins"""
    x=coordonnees[0]
    y=coordonnees[1]
    hauteur=len(tableau)
    longueur=len(tableau[0])
    assert 0<=coordonnees[0]<hauteur+1 and 0<=coordonnees[1]<longueur
    liste=[]
    for i in range(x-1, x+2):
        for j in range(y-1, y+2):
            liste.append((i,j))
    liste2=list(liste)
    #supprime les coordonnées hors du tableau + point en question
    for i in liste:
        if i[0]<0 or i[1]<0 or (i[0]==x and i[1]==y) or (i[0]>hauteur-1 or i[1]>longueur-1):
            liste2.remove(i)
    liste3=[(tableau[i[0]][i[1]]) for i in liste2]
    return liste3

class case:
    def __init__(self,est_bombe:bool, coordonnees, tableau=[]):
        self.tableau = tableau
        self.est_bombe=est_bombe
        self.coordonnees=coordonnees
        self.voisins= voisins(self.coordonnees,self.tableau)
        self.est_revelee=False
        if not self.est_bombe:
            self.nb=len(self.voisins)
            self.etat=str(self.nb)
        else:
            self.etat='Bombe'


    def vide(self):
        return self.nb==0

    def bombe(self):
        return self.est_bombe

    def __str__(self) -> str:
        return self.etat




#TESTS
tableau1=[]
for i in range(3):
    liste=[]
    for j in range(4):
        liste.append('')
    tableau1.append(liste)


for i in range(3):
    for j in range(4):
        b=case(False,(i,j),tableau1)
        tableau1[i][j]=b

a=case(True,(1,0),tableau1)
tableau1[1][0]=a

for i in range(len(tableau1)):
    for j in range(len(tableau1[0])):
        if j == len(tableau1[0])-1:
            print(tableau1[i][j])
        else:
            print(tableau1[i][j], end=',')

print('----------------------------------------------------------------')

print(voisins((0,0),tableau1)) 
print(tableau1[0][0].coordonnees)
print((tableau1[0][0]).voisins)