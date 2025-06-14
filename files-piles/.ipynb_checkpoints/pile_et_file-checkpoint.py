
class Pile:
    def __init__(self):
        self.elements = []

    def empiler(self, element):
        """Empile un élément sur le dessus de la pile."""
        self.elements.append(element)

    def depiler(self):
        """Dépile l'élément du dessus de la pile."""
        if not self.est_vide():
            return self.elements.pop()
        else:
            raise IndexError("La pile est vide.")

    def sommet(self):
        """Retourne l'élément au sommet de la pile sans le retirer."""
        if not self.est_vide():
            return self.elements[-1]
        else:
            raise IndexError("La pile est vide.")

    def est_vide(self):
        """Vérifie si la pile est vide."""
        return len(self.elements) == 0

    def __str__(self):
        return str(self.elements)

class File:
    def __init__(self):
        self.elements = []

    def enfiler(self, element):
        """Ajoute un élément à la fin de la file."""
        self.elements.append(element)

    def defiler(self):
        """Retire l'élément du début de la file."""
        if not self.est_vide():
            return self.elements.pop(0)
        else:
            raise IndexError("La file est vide.")

    def premier(self):
        """Retourne l'élément au début de la file sans le retirer."""
        if not self.est_vide():
            return self.elements[0]
        else:
            raise IndexError("La file est vide.")

    def est_vide(self):
        """Vérifie si la file est vide."""
        return len(self.elements) == 0

    def __str__(self):
        return str(self.elements)

# Exemple d'utilisation
if __name__ == "__main__":
    ma_pile = Pile()
    ma_pile.empiler(1)
    ma_pile.empiler(2)
    print("Pile avant dépilement:", ma_pile)
    print("Élément dépilé:", ma_pile.depiler())
    print("Pile après dépilement:", ma_pile)

    ma_file = File()
    ma_file.enfiler(1)
    ma_file.enfiler(2)
    print("File avant défiler:", ma_file)
    print("Élément défilé:", ma_file.defiler())
    print("File après défiler:", ma_file)
