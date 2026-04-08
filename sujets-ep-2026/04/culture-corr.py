#############################################################################
# Jeux de données fournis                                                   #
#############################################################################
from plantes import plantes
from mesures import mesures

#############################################################################
# Écrire le code de la fonction croissance_moyenne de la question 1         #
#############################################################################

def croissance_moyenne(liste_plantes):
    """Calcule la moyenne de durée de croissance (en jours) des plantes."""
    if not liste_plantes:
        return None
    somme = 0
    for plante in liste_plantes:
        somme += plante.croissance
    return somme / len(liste_plantes)

# On peut aussi utiliser sum() et une compréhension :
# def croissance_moyenne(liste_plantes):
#     if not liste_plantes:
#         return None
#     return sum(p.croissance for p in liste_plantes) / len(liste_plantes)


def test_croissance_moyenne():
    print("--- Test de croissance_moyenne ---")
    assert croissance_moyenne([]) is None, "Erreur sur la liste vide"
    # Avec les données de plantes.py (60 + 80 + 80 + 85 + 90) / 5 = 395 / 5 = 79.0
    assert croissance_moyenne(plantes) == 79.0, "Erreur sur le calcul de la moyenne"
    print("Tests croissance_moyenne OK !")

test_croissance_moyenne()


#############################################################################
# Écrire le code de la fonction dictionnaire_mesure de la question 2      #
#############################################################################

def dictionnaire_mesure(liste_plantes, liste_mesures):
    """Renvoie un dictionnaire regroupant les mesures par nom de plante."""
    # On initialise le dictionnaire avec toutes les plantes (listes vides)
    dico = {}
    for plante in liste_plantes:
        dico[plante.nom] = []
        
    # On la remplit avec les mesures correspondantes
    for mesure in liste_mesures:
        if mesure['plante'] in dico:
            dico[mesure['plante']].append(mesure)
            
    return dico

def test_dictionnaire_mesure():
    print("\n--- Test de dictionnaire_mesure ---")
    dico = dictionnaire_mesure(plantes, mesures)
    
    # On vérifie que toutes les plantes sont dans le dictionnaire
    assert set(dico.keys()) == {"Basilic", "Tomate", "Menthe", "Tournesol", "Fougère"}
    # La fougère n'a aucune mesure, on vérifie que sa liste est vide
    assert dico["Fougère"] == []
    # On vérifie une mesure pour le Basilic
    assert len(dico["Basilic"]) == 60
    assert dico["Basilic"][0]['plante'] == 'Basilic'
    print("Tests dictionnaire_mesure OK !")

test_dictionnaire_mesure()


#############################################################################
# Fonction défaillante à analyser et corriger pour les questions 3 et 4     #
#############################################################################

# Erreur de l'algorithme d'origine :
# La boucle "for mesure in liste_mesures" itère de manière séquentielle en
# avançant un index invisible. Lorsqu'on supprime un élément avec .remove(mesure), 
# tous les éléments suivants sont décalés d'un cran vers la gauche.
# Au tour de boucle suivant, l'index avance, et on "saute" donc l'analyse
# de l'élément qui vient de prendre la place de celui qu'on a supprimé.
# Cela se produit lorsque deux éléments à désactiver se suivent.

def purger_mesures_extremes(liste_mesures):
    """
    Supprime de la liste toutes les mesures dont la température 
    n'est pas comprise entre 20 et 25°C inclus.
    """
    # Solution la plus pythonique (et la plus sûre) : 
    # Filtrer par compréhension et renvoyer une nouvelle liste
    return [mesure for mesure in liste_mesures if 20 <= mesure['temperature'] <= 25]

    """
    # Alternative (modification en place de la liste d'origine) :
    # Si on souhaite modifier la liste en place, on peut la parcourir de la
    # fin vers le début (index inversé), ainsi un décalage éventuel à 
    # gauche n'impactera pas les éléments restant à visiter (ceux situés avant).
    for i in range(len(liste_mesures) - 1, -1, -1):
        if liste_mesures[i]['temperature'] < 20 or liste_mesures[i]['temperature'] > 25:
            del liste_mesures[i]
    return liste_mesures
    """

def test_purger():
    print("\n--- Test de purger_mesures_extremes ---")
    mesures_test = [
         {'jour': 1, 'plante': 'Basilic', 'temperature': 18.0}, # Va être supprimée
         {'jour': 2, 'plante': 'Basilic', 'temperature': 19.0}, # Va être supprimée (provoquait le bug initialement)
         {'jour': 3, 'plante': 'Basilic', 'temperature': 22.0}, # Conservée
         {'jour': 4, 'plante': 'Basilic', 'temperature': 28.0}, # Va être supprimée
         {'jour': 5, 'plante': 'Basilic', 'temperature': 29.0}  # Va être supprimée
    ]

    resultat = purger_mesures_extremes(mesures_test)

    print("Résultat après la purge :")
    for m in resultat:
        print(f"Jour {m['jour']} : {m['temperature']}°C")

test_purger()
