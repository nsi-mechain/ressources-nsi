class Arbre_binaire:
    def __init__(self, nom):
        self.nom = nom
        self.G = None
        self.D = None

    def hauteur(self):
        if self is None:
            return 0
        else:
            hauteur_gauche = self.G.hauteur() if self.G else 0
            hauteur_droite = self.D.hauteur() if self.D else 0
            return max(hauteur_gauche, hauteur_droite) + 1

    def taille(self):
        if self is None:
            return 0
        else:
            taille_gauche = self.G.taille() if self.G else 0
            taille_droite = self.D.taille() if self.D else 0
            return taille_gauche + taille_droite + 1

    def parcours_prefixe(self):
        parcours = []
        if self is not None:
            parcours.append(self.nom)
            parcours += self.G.parcours_prefixe() if self.G else []
            parcours += self.D.parcours_prefixe() if self.D else []
        return parcours

    def parcours_infixe(self):
        parcours = []
        if self is not None:
            parcours += self.G.parcours_infixe() if self.G else []
            parcours.append(self.nom)
            parcours += self.D.parcours_infixe() if self.D else []
        return parcours

    def parcours_postfixe(self):
        parcours = []
        if self is not None:
            parcours += self.G.parcours_postfixe() if self.G else []
            parcours += self.D.parcours_postfixe() if self.D else []
            parcours.append(self.nom)
        return parcours



####################### Tests ###########################
#
#           A
#        /     \
#       B       C
#      / \     /
#     D   E   F
#        /
#       G

arbre = Arbre_binaire("A")

arbre.G = Arbre_binaire("B")
arbre.G.G = Arbre_binaire("D")
arbre.G.D = Arbre_binaire("E")
arbre.G.D.G = Arbre_binaire("G")

arbre.D = Arbre_binaire("C")
arbre.D.G = Arbre_binaire("F")

print(arbre.hauteur())
print(arbre.taille())
print(arbre.parcours_prefixe())
print(arbre.parcours_infixe())
print(arbre.parcours_postfixe())
