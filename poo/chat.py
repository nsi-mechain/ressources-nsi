class Chat:
    def __init__(self, nom, sexe, masse):
        self.nom = nom
        self.sexe = sexe
        self.masse = masse

    def get_nom(self):
        return self.nom

    def get_sexe(self):
        return self.sexe

    def get_masse(self):
        return self.masse

    def grossir(self, poids):
        self.masse += poids

    def maigrir(self, poids):
        self.masse -= poids

    def __str__(self):
        return f"{self.nom} est un{'e' if self.sexe == 'femelle' else ''} {self.sexe} de {self.masse}kg"

    def __add__(self, autre):
        return Chat("mina", "femelle", 0.1)


chat1 = Chat("minou", "mâle", 5.0)
chat2 = Chat("minette", "femelle", 4.0)

print(chat1.get_nom(), "plus lourd que", chat2.get_nom(), "?", chat1.get_masse() > chat2.get_masse())
print("Sexes différents ?", chat1.get_sexe() != chat2.get_sexe())

chat1.grossir(0.2)
chat2.maigrir(0.15)

print("Après régime :")
print(chat1)
print(chat2)

mina = chat1 + chat2
mina.grossir(0.6)
print(mina)

del chat1
del chat2

try:
    print(chat1, chat2)
except NameError:
    print("les parents sont morts.")