class Wagon:
    def __init__(self, id, chargement):
        self.id = id
        self.chargement = chargement
        self.suivant = None

    def __repr__(self):
        return f'W{self.id}({self.chargement})'


class Train:
    def __init__(self, nom):
        self.nom = nom
        self.tete = None

    def ajoute(self, nouveau_wagon):
        if self.tete is None:
            self.tete = nouveau_wagon
        else:
            courant = self.tete
            while courant.suivant is not None:
                courant = courant.suivant
            courant.suivant = nouveau_wagon

    def retire(self, id):
        if self.tete is None:
            return
        elif self.tete.id == id:
            self.tete = self.tete.suivant
        else:
            courant = self.tete
            while courant.suivant is not None:
                if courant.suivant.id == id:
                    a_retirer = courant.suivant
                    courant.suivant = courant.suivant.suivant
                    a_retirer.suivant = None
                    return a_retirer
                courant = courant.suivant

    def __repr__(self):
        chaine = self.nom
        courant = self.tete
        while courant is not None:
            chaine += f" ➡ W{courant.id}({courant.chargement})"
            courant = courant.suivant
        return chaine


################################################################
train1 = Train('Laon-Amiens')

train1.ajoute(Wagon(123, 'blé'))
train1.ajoute(Wagon(219, 'charbon'))
train1.ajoute(Wagon(223, 'moutons'))
train1.ajoute(Wagon(116, 'moutons'))

print(train1)

wagon219 = train1.retire(219)
print(wagon219)

print(train1)

train2 = Train('Reims-Troye')
train2.ajoute(wagon219)
train2.ajoute(Wagon(244, 'sable'))

print(train2)