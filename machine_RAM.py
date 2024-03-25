class machine(object):

    def __init__(self, programme=[], entree=[]) -> None:
        
        self.prog = programme
        self.etape = 0
        self.entree = entree
        self.travail = [0]
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

    def valeur(self, val: str) -> int:
        if (registre := val[0]) == "R":
            return self.travail[int(val.split("R")[1])]
        elif registre == "I":
            return self.entree[int(val.split("I")[1])]
        elif registre == "O":
            return self.sortie[int(val.split("O")[1])]
        else:
            return int(val)
        
    def next(self):
        match self.get_instr().split("(")[0], self.get_instr().split("(")[1].split(")")[0].split(","):

            case["JE", args]:
                if self.valeur(args[0]) == self.valeur(args[1]):
                    self.set_etape(self.get_etape() + int(args[2]))

            case["ADD", args]:
                print("ADD ")
                if (registre := args[2]) == "R":
                    self.travail[int(args[2].split("R")[1])] = self.valeur(args[0]) + self.valeur(args[1])
                elif registre == "I":
                    self.entree[int(args[2].split("I")[1])] = self.valeur(args[0]) + self.valeur(args[1])
                elif registre == "O":
                    self.sortie[int(args[2].split("O")[1])] = self.valeur(args[0]) + self.valeur(args[1])
                    self.set_etape(self.get_etape() + 1)            

            case["JUMP", args]:
                    self.set_etape(self.get_etape() + int(args[2]))



    def __str__(self) -> str:
        output, ligne = "Programme:\n", 0
        for step in self.prog:
            output += str(ligne) + "   " + step + "\n"
            ligne += 1
        output += "Etape: " + str(self.etape) + "\n" + str(self.entree) + "  |  " + str(self.sortie)
        return output