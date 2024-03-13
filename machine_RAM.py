class machine(object):

    def __init__(self, programme=[], entree=[]) -> None:
        
        self.prog = programme
        self.etape = 0
        self.entree = entree
        self.sortie = []