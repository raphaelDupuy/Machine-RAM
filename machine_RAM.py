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
    
    def get_instr(self, etape=None) -> str:
        """Retourne l'instruction courante à effectuer par la machine si etape n'est pas spécifié sinon l'instruction à cette étape"""
        if etape != None:
            return self.prog[etape]
        else:
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
        
    def delete_instr(self, etape:int):
        """Retire l'instruction à l'étape donnée"""
        del self.prog[etape]
        
    def set_etape(self, nouvelle_etape):
        """Remplace l'étape courante par une nouvelle étape
        
        Arguments:
            nouvelle_etape (int): Nouvelle étape courante
        """
        self.etape = nouvelle_etape

    def set_instr(self, index:int, nouvelle_instr:str):
        """Remplace une instruction du programme à une étape donnée
        
        Arguments:
            index (int): Étape de l'instruction à remplacer
            nouvelle_instr (str): Instruction par laquelle remplacer l'ancienne
            """
        self.prog[index] = nouvelle_instr

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
        print(self.get_instr())
        match self.get_instr().split("(")[0], self.get_instr().split("(")[1].split(")")[0].split(","):
           
            case["JE", args]:
                if self.valeur(args[0]) == self.valeur(args[1]):
                    if (taille  := self.valeur(args[2])) < 0:
                        saut = taille - 1
                    else:
                        saut = taille + 1
                else:
                    saut = 1

            case["JUMP", args]:
                if (taille  := self.valeur(args[0])) < 0:
                    saut = taille - 1
                else:
                    saut = taille + 1

            case["ADD", args]:
                self.registre[self.adresse(args[2])] = self.valeur(args[0]) + self.valeur(args[1])
                saut = 1

            case["MULT", args]:
                self.registre[self.adresse(args[2])] = self.valeur(args[0]) * self.valeur(args[1])
                saut = 1

            case["DIV", args]:
                self.registre[self.adresse(args[2])] = self.valeur(args[0]) // self.valeur(args[1])
                saut = 1

            case["JL", args]:
                if self.valeur(args[0]) < self.valeur(args[1]):
                    if (taille  := self.valeur(args[2])) < 0:
                        saut = taille - 1
                    else:
                        saut = taille + 1
                else:
                    saut = 1
        
        self.set_etape(self.get_etape() + saut)

    def graphe(self) -> tuple:
        """Fonction d'affichage du graphe correspondant au programme RAM
        Le dernier état est l'état de Fin de programme

        Retoutne:
            (tuple): (sommets, arêtes) où somments est le nombre de sommets et arêtes est la liste des transitions
                    écrites dans un tuple de deux sommets (int, int)
        """
        aretes = []
        etape = 0
        programme = self.get_prog()
        sommets = len(programme)

        for index, instr in enumerate(programme):
            match instr.split("(")[0], instr.split("(")[1].split(")")[0].split(","):
                
                case["ADD", args]:
                    aretes.append((etape, etape+1))

                case["MULT", args]:
                    aretes.append((etape, etape+1))

                case["DIV", args]:
                    aretes.append((etape, etape+1))

                case["JUMP", args]:
                    valeur = self.valeur(args[0])
                    if valeur: 
                        saut = etape + valeur + (1 if valeur > 0 else (- 1 if valeur < 0 else 0))
                        if saut < 0:
                            saut = 0
                        elif saut > sommets:
                            saut = sommets
                        aretes.append((etape, saut))
                    else:
                        raise ValueError(f"Le JUMP à l'étape {index} est de taille 0")

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

        return(sommets, aretes)

    def detection_code_mort(self) -> set:
        """Fonction de détection du code mort
        
        Retourne:
            set(int): l'ensemble des états jamais accessibles dans le programme de la machine RAM
        """

        def etats_accessibles(etat_actuel:int) -> list:
            """Fonction de détection des états accessibles à partir d'un état donné et d'un ensemble de transitions.
               Cette fonction ne sert que dans le cadre de la détection de code mort.
            
            Arguments:
                transitions list[tuple]: transitions du graphe (état_départ, état_arrivée)
                etat_actuel (int): numéro correspondant à l'état à partir duquel nous voulons trouver les états accessibles

            Retourne:
                list[int]: liste des états accessibles à partir de l'état donné
            """
            accessibles = []
            for etat_depart, etat_arrivee in transitions:
                if etat_depart == etat_actuel:
                    accessibles.append(etat_arrivee)

            return accessibles
        

        taille, transitions = self.graphe()
        inaccessibles = set(i for i in range(1, taille + 1))
        actuels = [0]

        while actuels:
            nouveaux = []

            for etat in actuels:
                temp = etats_accessibles(etat)

                for e in temp:
                    if e in inaccessibles:
                        inaccessibles.remove(e)
                        nouveaux.append(e)
    
            actuels = nouveaux

        return inaccessibles
    
    def suppr(self, indexes:set):
        """Supprime les instructions aux indexes donnés dans le programme tout en conservant son bon fonctionnement
        
        Arguments:
            indexes (set): ensemble des indexes auquels supprimmer les instructions dans le programme
            """

        changements = []
        jumps_morts = []

        # Pour chaque instruction du programme
        for etape, instr in enumerate(self.get_prog()):

            # Si l'instruction contient un jump et qu'elle n'est pas une instruction morte
            if ((instruction := instr.split("(")[0]) in {"JUMP", "JE", "JL"}) and (etape not in indexes):

                # Récupérer la taille du jump
                if instruction == "JUMP":
                    taille = int(instr.split("(")[1].split(")")[0])
                    corps = "JUMP("
                else:
                    taille = int(instr.split("(")[1].split(")")[0].split(",")[2])
                    corps = str(instr.split(",")[0] + "," + instr.split(",")[1] + ",")

                signe = 1 if taille >= 0 else -1

                # Compter les instructions mortes dans le spectre du jump
                cnt = 0
                for i in range(signe, taille + signe, signe):
                    if (etape + i) in indexes:
                        cnt += 1

                # Stocker le changement de taille du jump si sa taille change apres suppression
                if cnt:
                    nouvelle_taille = (taille - (cnt * signe))

                    if nouvelle_taille:
                        nouvelle_instr = corps + str(nouvelle_taille) + ")"
                    else:
                        nouvelle_instr = 0

                    changements.append((etape, nouvelle_instr))

        # Effectuer les changements dans la mémoire de la machine
        for change in changements:
            if change[1]:
                self.set_instr(*change)
            else:
                jumps_morts.append(change[0])

        indexes = sorted(list(indexes), reverse=True)
        for etape in indexes:
            self.delete_instr(etape)

        if jumps_morts:
            self.suppr(set(jumps_morts))

        self.update_input()

    def optimisation(self):
        print("Optimisation du programme en cours...")

        get_arg = lambda i, j : self.get_instr(i).split("(")[1].split(")")[0].split(",")[j]
        sommets, transitions = self.graphe()
        suppr = set()

        # Pour chaque instruction
        for index in range(sommets):
            # Si l'instruction est un ADD
            if (self.get_instr(index).split("(")[0] == "ADD"):
                # On regarde ses prédecesseurs et on vérifie qu'il n'y en a qu'un seul et que c'est un ADD
                i = 0
                pred = None
                while (i < sommets):
                    if ((i, index) in transitions):
                        # Si ils écrivent dans le même registre
                        if (self.get_instr(i).split("(")[0] == "ADD") and (get_arg(i, 2) == get_arg(index, 2)):
                            registre = get_arg(index, 2)
                            pred = i
                        else:
                            pred, i = None, sommets
                    i += 1

            # On les fusionne si possible
            if pred is not None:

                nombre_registres = 0
                somme = 0
                args = [get_arg(pred, 0), get_arg(pred, 1), get_arg(index, 0), get_arg(index, 1)]
                position = None
                position_arrivée = None
                # On vérifie si un des arguments est un registre et si il est le seul et qu'il est différent du registre dans lequel l'instruction écrit
                for i in range(4):
                    if args[i][0] in {"I", "R", "O"}:
                        if args[i] == registre:
                            position_arrivée = i
                        else:
                            nombre_registres += 1
                            position = i
                    else:
                        somme += int(args[i])

                # On crée une nouvelle instruction en fonction de la présence d'un registre ou non
                if nombre_registres < 2:
                    if position is not None:
                        nouvelle_instr = f"ADD({args[position]},{somme},{registre})"
                        self.prog[index] = nouvelle_instr
                    elif position_arrivée is not None:
                        nouvelle_instr = f"ADD({somme},0,{registre})"
                        self.prog[index] = nouvelle_instr
                    suppr.add(pred)

        if len(suppr):
            self.suppr(suppr)
            print((f"Optimisation terminée, {len(suppr)} changements effectués.\n"))
            print(f"Graphe (Nb de sommets, transitions):\n{self.graphe()}\n")
        else:
            print("Optimisation terminée, aucun changements effectués.\n")

    def update_input(self):
        file = open("input.1", "w")
        entree = ""
        for elem in self.get_entree():
            entree += str(elem.split(":")[1] + ",")
        entree = entree[:-1]

        entree += "\n"
        for instr in self.get_prog():
            entree += instr + "\n"
        entree = entree[:-1]

        file.write(entree)
        file.close()
                


    def calcule(self):
        """Éxecute le programme RAM de la machine
        
        Retourne:
            print: Configuration lisible de la machine à chaque étape puis registre Sortie à la fin du programme
        """

        print(f"Graphe (Nb de sommets, transitions):\n{str(graphe := self.graphe())}\n")

        # Si Il existe des états inaccessibles dans le graphe du programme
        if (indexes := self.detection_code_mort()):

            non_acc = []
            # Pour chaque états non accessible
            for i in indexes:

                # Si Cet état est l'état final: Erreur
                if i == graphe[0]:
                    raise SyntaxError("Le programme ne termine jamais")
                # Sinon stocker l'instruction non accessible à partir de son index
                else:
                    non_acc.append(self.get_instr(i))
            
            supp = str(input(f"Les instructions suivantes ne sont jamais accessibles: {non_acc}\nEtape(s):  {indexes}\nSupprimmer les instructions inaccessibles ?\ny: oui, sinon passer\n  >"))

            # On réécrit le contenu de la machine dans le programme input
            if supp == "y":
                print("Suppression du code mort.\n")
                self.suppr(indexes)
                self.optimisation()
                self.calcule()

        else:
            print("Éxecution du programme")
            print("Aucun code mort détecté\n")
            self.optimisation()


            while self.get_etape() < len(self.prog):
                self.next()
                self.affiche_config()

            print("Sortie : " + str(self.get_sortie()))
