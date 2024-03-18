class machine(object):

    def __init__(self, programme=[], entree=[]) -> None:
        
        self.prog = programme
        self.etape = 0
        self.entree = entree
        self.sortie = []

    def get_etape(self) -> int:
        return self.etape
    
    def get_sortie(self) -> list:
        return self.sortie
    
    def get_entree(self, pointeur):
        return self.entree[pointeur]

    def __str__(self) -> str:
        output, ligne = "Programme:\n", 0
        for step in self.prog:
            output += str(ligne) + "   " + step + "\n"
            ligne += 1
        output += "Etape: " + str(self.etape) + "\n" + str(self.entree) + "  |  " + str(self.sortie)
        return output