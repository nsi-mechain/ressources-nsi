# Projet Terminale NSI
## Prévisions météorologiques

### Thèmes abordés :

- Programmation en langage *Python*
- format JSON
- Bases de données *SQLite*

### Description :

À partir de l'API disponible sur [Météo Concept](https://api.meteo-concept.com/), réalisez une application qui permettra de choisir 2 communes (à partir de leurs codes INSEE) pour en effectuer les **prévisions météorologiques comparatives**.

### Spécifications et contraintes :

- Les prévisions météorologiques de ces villes seront enregistrées dans une BDD *SQlite* Qui contiendra 3 tables :
  - 1 table **meteo** de prévisions à 14 jours pour les deux villes
  - 1 table **villes** contenant les informations géographiques
  - 1 table **codes** contenant les "codes temps" (voir aide en fin de page)

### Groupes et durée

- binômes
- 2 séances de 2 heures

### Évaluation

- Oral avec support numérique projeté (diaporama, page web, etc.)
- Durée : 15 minutes par binôme

### Aide

- Présentation du format JSON : [lien](https://www.json.org/json-fr.html)
- Éditeur et validateur JSON en ligne : [lien](https://omute.net/editor)

- Un script *Python* récupérant la météo à 14 jours pour la ville de Laon :

```python
from urllib.request import urlopen
import json

token = 'ee26c8f341de6ae95011bdf65a7479408fe52e3bf81885a13bc770ab3e007678'
INSEE = '02408'  # Laon
url = f'https://api.meteo-concept.com/api/forecast/daily?token={token}&insee={INSEE}'
retour = urlopen(url).read()
dico = json.loads(retour)

print(type(retour), type(dico))
print()
print(retour.decode("utf-8"))
print()
print(dico)
```

- La table des **codes temps** de *Meteo Concept* : [codes_temps.csv](codes_temps.csv)

---
