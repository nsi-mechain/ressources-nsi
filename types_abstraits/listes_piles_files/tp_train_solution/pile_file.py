class Pile:
   def __init__(self):
       self.elements = []

   def empile(self, element):
       self.elements.append(element)

   def depile(self):
       if len(self.elements) > 0:
           return self.elements.pop()
       else:
           return None

   def taille(self):
       return len(self.elements)

   def est_vide(self):
       return len(self.elements) == 0


class File:
  def __init__(self):
      self.elements = []

  def enfile(self, element):
      self.elements.append(element)

  def defile(self):
      if len(self.elements) > 0:
          return self.elements.pop(0)
      else:
          return None

  def taille(self):
      return len(self.elements)

  def est_vide(self):
      return len(self.elements) == 0
  

class Wagon:
    def __init__(self, id, chargement):
        self.id = id
        self.chargement = chargement
        self.suivant = None

    def __repr__(self):
        return f'W{self.id}({self.chargement})'


class Voie_sans_issue:
    def __init__(self, nom):
        self.nom = nom
        self.pile_de_wagons = Pile()

    def ajoute(self, nouveau_wagon):
        self.pile_de_wagons.empile(nouveau_wagon)

    def retire(self):
        return self.pile_de_wagons.depile()

    def __repr__(self):
        #wagons = self.pile_de_wagons.elements
        if self.pile_de_wagons.est_vide():
            return f'La voie sans issue {self.nom} est vide'
        else:
            return f'La voie sans issue {self.nom} contient : {" ➡ ".join([str(w) for w in self.pile_de_wagons.elements])}'



class Voie_de_garage:
    def __init__(self, nom):
        self.nom = nom
        self.file_de_wagons = File()

    def ajoute(self, nouveau_wagon):
        self.file_de_wagons.enfile(nouveau_wagon)

    def retire(self):
        return self.file_de_wagons.defile()

    def __repr__(self):
        if self.file_de_wagons.est_vide():
            return f'La voie de garage {self.nom} est vide'
        else:
            return f'La voie de garage {self.nom} contient : {" ➡ ".join([str(w) for w in self.file_de_wagons.elements])}'


##########################################################

wagon123 = (Wagon(123, 'blé'))
wagon219 = (Wagon(219, 'charbon'))
wagon223 = (Wagon(223, 'moutons'))
wagon116 = (Wagon(116, 'moutons'))


voie1 = Voie_sans_issue('voie1')
voie1.ajoute(wagon123)
voie1.ajoute(wagon219)
voie1.ajoute(wagon223)
print(voie1)

voie1.retire()
print(voie1)

voie1.retire()
voie1.retire()
print(voie1)

print()

voie2 = Voie_de_garage('voie2')
voie2.ajoute(wagon123)
voie2.ajoute(wagon219)
voie2.ajoute(wagon223)
print(voie2)

voie2.retire()
print(voie2)

voie2.retire()
voie2.retire()
print(voie2)

print()

voie1.ajoute(wagon123)
voie1.ajoute(wagon219)
print(voie1)
print(voie2)
voie2.ajoute(voie1.retire())
print(voie1)
print(voie2)
voie2.ajoute(voie1.retire())
print(voie1)
print(voie2)




