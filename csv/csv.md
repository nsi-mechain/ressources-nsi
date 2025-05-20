# Fichiers CSV et Python

1. Fichiers CSV (voir [ici](https://fr.wikipedia.org/wiki/Comma-separated_values)).

---

2. Rappel : Lecture et écriture dans un fichier texte en Python :
   - Créez un programme `wt.py` qui enregistre dans un fichier texte "t.txt" un petit texte entré au clavier.
   - Créez un programme `rt.py` qui affiche à l'écran le texte contenu dans "t.txt".
   - Ajoutez les "sécurités nécessaires" à ces deux programmes (vérification de l'existence).

---

3. Copié-collé (collage texte brut) de l'exemple de *Wikipédia* dans le tableur *Libreoffice Calc*. Export en CSV, puis ouverture avec éditeur de texte pour vérification et modification manuelle.
   ---
4. Lecture et écriture de fichiers CSV en *Python*  (utilisez le [module csv](https://docs.python.org/fr/3/library/csv.html)) :
   - Lecture d'un CSV (reprendre l'exemple *Wikipédia* en l'étoffant pour avoir 10 enregistrements) et création d'une **liste de dictionnaires** (dont les clés sont les noms des colonnes) en Python.
   - Création d'un CSV à partir d'une **liste de dictionnaires** en Python
   - Sélection et affichage des enregistrements vérifiant le critère **personnes nées après 1970**
   - Affichage des noms par **âges croissants** des personnes enregistrées

---

5. Application :
   - En *Python*, concevez un programme permettant d'obtenir un fichier CSV qui contiendra 20 enregistrements. Ces enregistrements indiqueront la date, l'heure, la mémoire vive utilisée (en %) et l'utilisation du CPU (en %)  pendant une minute (un enregistrement toutes les trois secondes). Utilisez les modules *psutils*, *datetime* et *time*.
   - Avec un tableur (*libreoffice Calc*), tracez le graphe d'utilisation de la RAM et du CPU en fonction de l'heure.
   - Travail complémentaire (si vous avez fini ce qui précède) : Effectuez ce tracé avec un programme python utilisant *matplotlib*.
