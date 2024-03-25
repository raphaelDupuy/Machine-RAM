class machine(object):

    def __init__(self, programme=[], entree=[]) -> None:
        
        self.prog = programme
        self.etape = 0
        self.entree = entree
        self.sortie = []

    def get_etape(self) -> int:
        return self.etape
    
    def get_instr(self):
        return self.prog[self.etape]
    
    def get_sortie(self, pointeur=None) -> list|str:
        if pointeur != None:
            return self.sortie[pointeur]
        else:
            return self.sortie
    
    def get_entree(self, pointeur=None) -> str:
        if pointeur != None:
            return self.entree[pointeur]
        else:
            return self.entree
        
    def set_etape(self, nouvelle_etape):
        self.etape = nouvelle_etape
        
    def next(self):
        print(self.get_instr().split("(")[1].split(")")[0])
        match self.get_instr().split("(")[1].split(")")[0]:
            case["JE", args]:
                print("JE" + args)
            case["ADD", args]:
                print("ADD" + args)
            case["JUMP", args]:
                print("JUMP" + args)


    def __str__(self) -> str:
        output, ligne = "Programme:\n", 0
        for step in self.prog:
            output += str(ligne) + "   " + step + "\n"
            ligne += 1
        output += "Etape: " + str(self.etape) + "\n" + str(self.entree) + "  |  " + str(self.sortie)
        return output