class Arbre_binaire:
    def __init__(self, nom):
        self.nom = nom
        self.G = None
        self.D = None

def hauteur(arbre):
    if arbre is None:
        return 0
    else:
        hauteur_gauche = hauteur(arbre.G)
        hauteur_droite = hauteur(arbre.D)
        return max(hauteur_gauche, hauteur_droite) + 1

def taille(arbre):
    if arbre is None:
        return 0
    else:
        taille_gauche = taille(arbre.G)
        taille_droite = taille(arbre.D)
        return taille_gauche + taille_droite + 1

def parcours_prefixe(arbre):
    parcours = []
    if arbre is not None:
        parcours.append(arbre.nom)
        parcours += parcours_prefixe(arbre.G)
        parcours += parcours_prefixe(arbre.D)
    return parcours

def parcours_infixe(arbre):
    parcours = []
    if arbre is not None:
        parcours += parcours_infixe(arbre.G)
        parcours.append(arbre.nom)
        parcours += parcours_infixe(arbre.D)
    return parcours

def parcours_postfixe(arbre):
    parcours = []
    if arbre is not None:
        parcours += parcours_postfixe(arbre.G)
        parcours += parcours_postfixe(arbre.D)
        parcours.append(arbre.nom)
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

print(hauteur(arbre))
print(taille(arbre))
print(parcours_prefixe(arbre))
print(parcours_infixe(arbre))
print(parcours_postfixe(arbre))
