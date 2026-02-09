class Wagon:
    def __init__(self, id, chargement):
        ...

    def __str__(self):
        ...


class Train:
    def __init__(self, nom):
        ...

    def ajoute(self, nouveau_wagon):
        ...

    def retire(self, id):
        ...

    def __str__(self):
        ...


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