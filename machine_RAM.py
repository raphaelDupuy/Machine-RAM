class machine(object):

    def __init__(self, programme=[], entree=[]) -> None:
        
        self.prog = programme
        self.etape = 0
    
        self.entree = {}
        indice = 0
        for elt in entree:
            self.entree["I" + str(indice)] = elt
            indice += 1
        
        self.travail = {}
        self.sortie = {}
    
    def __str__(self) -> str:
        output, ligne = "Programme:\n", 0
        for step in self.prog:
            output += str(ligne) + "   " + step + "\n"
            ligne += 1
        output += "Etape: " + str(self.get_etape() - 1) + "\n I " + str(self.get_entree()) + "  |  T " + str(self.get_travail()) +"  |  O " + str(self.get_sortie()) + "\n"
        return output

    def get_etape(self) -> int:
        return self.etape
    
    def get_instr(self):
        return self.prog[self.etape]
    
    def get_sortie(self, pointeur=None) -> dict|int:
        if pointeur != None:
            return self.sortie["O" + str(pointeur)]
        else:
            return self.sortie
        
    def get_travail(self, pointeur=None) -> dict|int:
        if pointeur != None:
            return self.travail["R" + str(pointeur)]
        else:
            return self.travail 
    
    def get_entree(self, pointeur=None) -> dict|int:
        if pointeur != None:
            return self.entree["I" + str(pointeur)]
        else:
            return self.entree
        
    def set_etape(self, nouvelle_etape):
        self.etape = nouvelle_etape

    def valeur(self, val: str) -> int:
        if (registre := val[0]) == "R":
            return self.travail[val]
        elif registre == "I":
            return self.entree[val]
        elif registre == "O":
            return self.sortie[val]
        else:
            return int(val)
        
    def next(self):
        match self.get_instr().split("(")[0], self.get_instr().split("(")[1].split(")")[0].split(","):

            case["JE", args]:
                print("JE")
                if self.valeur(args[0]) == self.valeur(args[1]):
                    self.set_etape(self.get_etape() + int(args[2]))
                else:
                    self.set_etape(self.get_etape() + 1)            

            case["ADD", args]:
                print("ADD")
                if (registre := args[2][0]) == "R":
                    self.travail[args[2]] = self.valeur(args[0]) + self.valeur(args[1])
                elif registre == "I":
                    self.entree[args[2]] = self.valeur(args[0]) + self.valeur(args[1])
                elif registre == "O":
                    self.sortie[args[2]] = self.valeur(args[0]) + self.valeur(args[1])
                self.set_etape(self.get_etape() + 1)            

            case["JUMP", args]:
                print("JUMP")
                self.set_etape(self.get_etape() + int(args[0]))

    def calcule(self):
        while self.get_etape() < len(self.prog):
            self.next()
            print(self)
        print("Output : " + str(self.get_sortie()))
