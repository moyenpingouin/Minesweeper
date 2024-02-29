class case:
    def __init__(self):
        self.etat='0'
        self.est_revelee=False

    def __str__(self):
        return self.etat

    def est_bombe(self):
        return False

class bombe:
    def __init__(self):
        self.etat='bombe'
        self.est_revelee=False

    def __str__(self):
        return self.etat

    def est_bombe(self):
        return True