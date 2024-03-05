from PIL import Image
class case:
    def __init__(self):
        self.ancien_etat='case'
        self.nouvel_etat=''
        self.est_revelee=False
        self.drapeau=False
        self.image=Image.open('images/case.png') #afficher_image(self): self.image.show()

    def __str__(self):
        if self.est_revelee==True:
            return self.nouvel_etat
        else:
            return 'X'

    def est_bombe(self):
        return False
    


class bombe:
    def __init__(self):
        self.nouvel_etat='b'
        self.est_revelee=False
        self.drapeau=False
        self.image=Image.open('images/case.png')
   

    def __str__(self):
        if self.est_revelee==True:
            return self.nouvel_etat
        else:
            return 'X'

    def est_bombe(self):
        return True


class tableau_rgt:
    def __init__(self,table):
        self.elem=table
    
    def test_revele(self):
        for i in range(len(self.elem)):
            for j in range(len(self.elem[0])):
                if not self.elem[i][j].nouvel_etat=='b':
                    if not self.elem[i][j].est_revelee:
                        return False
        return True