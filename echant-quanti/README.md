# Numérisation d'un signal analogique

Ce programme en Python génère et visualise un signal analogique ainsi qu'une version quantifiée de ce signal.

1. **Imports des bibliothèques nécessaires** :
   - `numpy` pour les calculs mathématiques et la manipulation de tableaux.
   - `matplotlib.pyplot` pour la création de graphiques.

2. **Définitions des paramètres** :
   - `n_bits = 4` : Le nombre de bits utilisé pour la quantification (résolution du signal quantifié).
   - `nb_echant = 20` : Le nombre d'échantillons utilisé pour représenter le signal quantifié.

3. **Définition de la fonction du signal analogique** :
   - La fonction `f(t)` définit un signal analogique basé sur une combinaison de sinus (harmoniques). Le signal est défini entre 0 et 1 pour les valeurs de `t` allant de 0 à 1.

4. **Génération du signal analogique** :
   - Des valeurs de `x` sont générées entre 0 et 1 avec un pas de 0,01.
   - Les valeurs correspondantes de `y` sont calculées en utilisant la fonction `f(t)` et sont multipliées par `(2 ** n_bits - 1)` pour obtenir une amplitude convenable en vue de la quantification.

5. **Visualisation du signal analogique** :
   - Ce signal est dessiné sur un graphique avec une ligne bleue épaisse.

6. **Génération du signal quantifié** :
   - Des valeurs de `x` sont générées entre 0 et 1 avec un pas égal à `1 / nb_echant`, correspondant au nombre d'échantillons souhaités.
   - Les valeurs de `y` sont arrondies (`np.round`) pour représenter la version quantifiée du signal analogique.

7. **Visualisation du signal quantifié** :
   - Les points du signal échantillonné et quantifié sont représentés par des cercles rouges sur le graphique.

8. **Personnalisation des axes** :
   - L'axe des `y` affiche des graduations correspondant aux valeurs discrètes (quantifiées) avec une étiquette en code binaire (`n_bits` bits).
   - L'axe des `x` affiche des graduations correspondant aux échantillons.

9. **Ajout de grilles** :
   - Une grille horizontale (axe `y`) est ajoutée en rouge pour aider à visualiser les niveaux de quantification.
   - Une grille verticale (axe `x`) est ajoutée en pointillés pour marquer les positions des échantillons.

10. **Affichage du graphique** :
    - Le graphique est affiché avec les deux signaux (analogique et quantifié).

### Résultat attendu :
- Un graphique montrant un signal analogique sinusoidal bleu.
- Une version echantillonnée et quantifiée de ce signal superposée sous forme de points rouges.
- Les graduations de l'axe des `y` sont affichées en code binaire, ce qui reflète la quantification en fonction des bits définis (`n_bits = 4`).
