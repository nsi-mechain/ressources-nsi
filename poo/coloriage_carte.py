# Inspiré du sujet de bac NSI 2023 : NSIJ1ME1
# Sujet : https://pixees.fr/informatiquelycee/term/suj_bac/2023/sujet_07.pdf
# Corrigé : https://pixees.fr/informatiquelycee/term/suj_bac/2023/correction_sujet_07.pdf


class Region:
    def __init__(self, nom_region):
        self.nom = nom_region
        self.tab_voisines = []
        self.tab_couleurs_disponibles = ['rouge', 'vert', 'bleu', 'jaune']
        self.couleur_attribuee = None
        
    def __repr__(self):
        return self.nom
     
    def renvoie_premiere_couleur_disponible(self):
        return self.tab_couleurs_disponibles[0]

    def renvoie_nb_voisines(self) :
        return len(self.tab_voisines)

    def est_coloriee(self):
        return self.couleur_attribuee != None

    def retire_couleur(self, couleur):
        if couleur in self.tab_couleurs_disponibles:
            self.tab_couleurs_disponibles.remove(couleur)

    def est_voisine(self, region):
        for r in self.tab_voisines:
            if r == region:
                return True
        return False


class Pays:
    def __init__(self, tab_regions):
        self.tab_regions = tab_regions
          
    def renvoie_tab_regions_non_coloriees(self):
        tab_r =[]
        for r in self.tab_regions:
            if not r.est_coloriee():
                tab_r.append(r)
        return tab_r

    def renvoie_max(self):
        nb_voisines_max = -1
        region_max = None
        for reg in self.renvoie_tab_regions_non_coloriees():
            if reg.renvoie_nb_voisines() > nb_voisines_max:
                nb_voisines_max = reg.renvoie_nb_voisines()
                region_max = reg
        return region_max

    def colorie(self):
        r_max = self.renvoie_max()
        while r_max != None:
            couleur = r_max.renvoie_premiere_couleur_disponible()
            r_max.couleur_attribuee = couleur
            for r in r_max.tab_voisines :
                r.retire_couleur(couleur)
            r_max = self.renvoie_max()


A = Region("Bretagne")
B = Region("Normandie")
C = Region("Hauts-de-France")
D = Region("Pays de la Loire")
E = Region("Centre Val-de-Loire")
F = Region("Île-de-France")
G = Region("Grand Est")
H = Region("Nouvelle-Aquitaine")
I = Region("Auvergne-Rhône-Alpes")
J = Region("Bourgogne-Franche-Comté")
K = Region("Occitanie")
L = Region("Provence-Alpes-Côte-d'Azur")

A.tab_voisines = [B,D]
B.tab_voisines = [A,D,E,F,C]
C.tab_voisines = [B,F,G]
D.tab_voisines = [A,B,E,H]
E.tab_voisines = [D,B,F,J,I,H]
F.tab_voisines = [B,C,G,J,E]
G.tab_voisines = [C,F,J]
H.tab_voisines = [D,E,I,K]
I.tab_voisines = [L,K,H,E,J]
J.tab_voisines = [I,E,F,G]
K.tab_voisines = [H,I,L]
L.tab_voisines = [K,I]

laFrance = Pays([A, B, C, D, E, F, G, H, I, J, K, L])

laFrance.colorie()

for region in laFrance.tab_regions:
    print(f'{region.nom:>26} : {region.couleur_attribuee}')
