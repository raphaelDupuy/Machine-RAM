class machine(object):

    def __init__(self, programme=[], entree=[]) -> None:
        
        self.prog = programme
        self.etape = 0
    
        self.registre = {}
        indice = 0
        for elt in entree:
            self.registre["I" + str(indice)] = elt
            indice += 1
    
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
    
    def get_registre(self):
        return self.registre
    
    def get_sortie(self, pointeur=None) -> list|int:
        if pointeur != None:
            return self.registre["O" + str(pointeur)]
        else:
            return [(str(k) + " :" + str(v)) for k, v in self.get_registre().items() if k[0] == "O"]
        
    def get_travail(self, pointeur=None) -> list|int:
        if pointeur != None:
            return self.registre["R" + str(pointeur)]
        else:
            return [(str(k) + " :" + str(v)) for k, v in self.get_registre().items() if k[0] == "R"]
    
    def get_entree(self, pointeur=None) -> list|int:
        if pointeur != None:
            return self.registre["I" + str(pointeur)]
        else:
            return [(str(k) + " :" + str(v)) for k, v in self.get_registre().items() if k[0] == "I"]
        
    def set_etape(self, nouvelle_etape):
        self.etape = nouvelle_etape

    def valeur(self, val: str) -> int:
        if val[0] in ("R", "I", "O"):
            if val[1] == "@":
                return self.registre[val[0] + str(self.valeur(val.split("@")[1]))]
            else:
                return self.registre[val]
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
                if args[2][0] in ("R", "I", "O"):
                    self.registre[args[2]] = self.valeur(args[0]) + self.valeur(args[1])
                self.set_etape(self.get_etape() + 1)            

            case["JUMP", args]:
                print("JUMP")
                self.set_etape(self.get_etape() + int(args[0]))

    def calcule(self):
        while self.get_etape() < len(self.prog):
            self.next()
            print(self)
        print("Output : " + str(self.get_sortie()))
