class Machine(object):
    """Classe représentant une machine RAM
    
    Attributs:
    ---------
    programme (list[str]): Liste d'instructions RAM
    etape (int): Étape courante de la machine (instructions numérotées à partir de 0)
    registre (dict{str: int}): Représentation de la mémoire de la machine sous forme de registres I, R et O
    """

    def __init__(self, programme=[], entree=[]) -> None:
        """Initialise une instance de la classe Machine
        
        Parametres:
            programme (list[str]): Liste d'instructions respectant la forme décrite dans le README
            entree (list[int]): Valeurs présentes dans le registre d'entrée
        """
        
        self.prog = programme
        self.etape = 0
    
        self.registre = {}

        # Ajoute le contenu de l'entrée dans le registre de la machine
        for indice, elt in enumerate(entree):
            self.registre["I" + str(indice)] = elt
    
    def __str__(self) -> str:
        """Retourne la représentation d'un objet Machine sous forme de chaîne de caractères"""
        output, ligne = "Programme:\n", 0
        for step in self.prog:
            output += str(ligne) + "   " + step + "\n"
            ligne += 1
        output += "Etape: " + str(self.get_etape() - 1) + "\n I " + str(self.get_entree()) + "  |  T " + str(self.get_travail()) +"  |  O " + str(self.get_sortie()) + "\n"
        return output
    
    def __repr__(self) -> str:
        """Retourne la représentation d'un objet de la classe Machine"""
        return f"Etape {self.get_etape()}, Registre: {self.get_registre()}\nEntrée: {self.get_entree()}     Travail: {self.get_travail()}     Sortie: {self.get_sortie()}"

    def affiche_config(self):
        """Retourne la configuration courante de la machine (Étape et état des registres)"""
        print(f"Etape: {self.get_etape()}\nI {self.get_entree()}\nT {self.get_travail()}\nO {self.get_sortie()}\n")

    def get_prog(self):
        """Retourne le programme RAM"""
        return self.prog

    def get_etape(self) -> int:
        """Retourne l'étape courante de la machine"""
        return self.etape
    
    def get_instr(self) -> str:
        """Retourne l'instruction courante à effectuer par la machine"""
        return self.prog[self.etape]
    
    def get_registre(self) -> dict:
        """Retourne l'ensemble de la mémoire de la machine
        
        Retourne:
            dict ({str: int}): Le str représente l'emplacement en mémoire (Registre et numérotation) et le int la valeur stockée
        """
        return self.registre
    
    def get_sortie(self, pointeur=None) -> list|int:
        """Retourne l'ensemble du registre O de la machine ou un seul élement de ce registre
        
        Arguments:
            pointeur (int): Emplacement de la valeur à retourner
                (None par défaut)
        
        Retourne:
            list[str]|int: Liste contenant les valeurs stockées dans le registre et leur numérotation ou simplement la valeur voulue
        """

        if pointeur != None:
            return self.registre["O" + str(pointeur)]
        else:
            return [(str(k) + " :" + str(v)) for k, v in self.get_registre().items() if k[0] == "O"]
        
    def get_travail(self, pointeur=None) -> list|int:
        """Retourne l'ensemble du registre R de la machine ou un seul élement de ce registre
        
        Arguments:
            pointeur (int): Emplacement de la valeur à retourner
                (None par défaut)
        
        Retourne:
            list[str]|int: Liste contenant les valeurs stockées dans le registre et leur numérotation ou simplement la valeur voulue
        """

        if pointeur != None:
            return self.registre["R" + str(pointeur)]
        else:
            return [(str(k) + " :" + str(v)) for k, v in self.get_registre().items() if k[0] == "R"]
    
    def get_entree(self, pointeur=None) -> list|int:
        """Retourne l'ensemble du registre I de la machine ou un seul élement de ce registre
        
        Arguments:
            pointeur (int): Emplacement de la valeur à retourner
                (None par défaut)
        
        Retourne:
            list[str]|int: Liste contenant les valeurs stockées dans le registre et leur numérotation ou simplement la valeur voulue
        """

        if pointeur != None:
            return self.registre["I" + str(pointeur)]
        else:
            return [(str(k) + " :" + str(v)) for k, v in self.get_registre().items() if k[0] == "I"]
        
    def set_etape(self, nouvelle_etape):
        """Remplace l'étape courante par une nouvelle étape
        
        Arguments:
            nouvelle_etape (int): Nouvelle étape courante
        """
        self.etape = nouvelle_etape

    def adresse(self, val: str) -> str:
        """Retourne l'adresse donnée ou l'adresse indirecte

        Arguments:
            val (str): Adresse directe OU Adresse indirecte

        Retourne:
            str: Adresse directe donnée OU adresse pointée par l'indirection
        """

        if val[0] in ("R", "I", "O"):
            if val[1] == "@":
                return str(val[0]) + str(self.valeur(val.split("@")[1]))
            else:
                return val

    def valeur(self, val: str) -> int:
        """Retourne la valeur stockée à un indice dans un registre donné ou une valeur donnée
        
        Arguments:
            val (str): Adresse directe OU Adresse indirecte OU Valeur entière sous forme de string

        Retourne:
            int: Valeur donnée ou stockée à l'emplacement donné
        """

        if val[0] in ("R", "I", "O"):
            if val[1] == "@":
                return self.registre[val[0] + str(self.valeur(val.split("@")[1]))]
            else:
                return self.registre[val]
        else:
            return int(val)
        
    def next(self):
        """Éxecute l'instruction à l'étape courante"""

        saut = 0
        match self.get_instr().split("(")[0], self.get_instr().split("(")[1].split(")")[0].split(","):

            case["JE", args]:
                print("JE")
                if self.valeur(args[0]) == self.valeur(args[1]):
                    if (taille  := self.valeur(args[2])) < 0:
                        saut = taille - 1
                    else:
                        saut = taille + 1
                else:
                    saut = 1

            case["JUMP", args]:
                print("JUMP")
                if (taille  := self.valeur(args[0])) < 0:
                    saut = taille - 1
                else:
                    saut = taille + 1

            case["ADD", args]:
                print("ADD")
                self.registre[self.adresse(args[2])] = self.valeur(args[0]) + self.valeur(args[1])
                saut = 1

            case["MULT", args]:
                print("MULT")
                self.registre[self.adresse(args[2])] = self.valeur(args[0]) * self.valeur(args[1])
                saut = 1

            case["DIV", args]:
                print("DIV")
                self.registre[self.adresse(args[2])] = self.valeur(args[0]) // self.valeur(args[1])
                saut = 1

            case["JL", args]:
                print("JL")
                if self.valeur(args[0]) < self.valeur(args[1]):
                    if (taille  := self.valeur(args[2])) < 0:
                        saut = taille - 1
                    else:
                        saut = taille + 1
                else:
                    saut = 1
        
        self.set_etape(self.get_etape() + saut)

    def graphe(self):
        """Fonction d'affichage du graphe correspondant au programme RAM
        Le dernier état est l'état de Fin de programme
        """
        
        aretes = []
        etape = 0
        programme = self.get_prog()
        sommets = len(programme)

        for instr in programme:
            match instr.split("(")[0], instr.split("(")[1].split(")")[0].split(","):
                
                case["ADD", args]:
                    aretes.append((etape, etape+1))

                case["MULT", args]:
                    aretes.append((etape, etape+1))

                case["DIV", args]:
                    aretes.append((etape, etape+1))

                case["JUMP", args]:
                    valeur = self.valeur(args[0])
                    saut = etape + valeur + (1 if valeur > 0 else (- 1 if valeur < 0 else 0))
                    if saut < 0:
                        saut = 0
                    elif saut > sommets:
                        saut = sommets
                    aretes.append((etape, saut))

                case["JE", args]:
                    valeur = self.valeur(args[2])
                    saut = etape + valeur + (1 if valeur > 0 else (- 1 if valeur < 0 else 0))
                    if saut < 0:
                        saut = 0
                    elif saut > sommets:
                        saut = sommets
                    aretes.append((etape, etape + 1))
                    aretes.append((etape, saut))

                case["JL", args]:
                    valeur = self.valeur(args[2])
                    saut = etape + valeur + (1 if valeur > 0 else (- 1 if valeur < 0 else 0))
                    if saut < 0:
                        saut = 0
                    elif saut > sommets:
                        saut = sommets
                    aretes.append((etape, etape + 1))
                    aretes.append((etape, saut))

            etape += 1       

        print(sommets, aretes)

    def calcule(self):
        """Éxecute le programme RAM de la machine
        
        Retourne:
            print: Configuration lisible de la machine à chaque étape puis registre Sortie à la fin du programme
        """

        while self.get_etape() < len(self.prog):
            self.next()
            self.affiche_config()
        
        self.graphe()
        print("Sortie : " + str(self.get_sortie()))

