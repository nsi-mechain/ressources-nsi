# Gestion des Processus sous Linux

**Niveau :** Terminale NSI

**Thème :** OS / Gestion des processus et ressources

## Objectifs

* Manipuler les commandes d'observation (`ps`, `top`, `htop`).
* Comprendre la hiérarchie Père/Fils.
* Gérer les signaux d'arrêt (`kill`).
* Différencier les états d'un processus.

---

## 1. Observation du système avec `ps`

La commande `ps` (Process Status) affiche un instantané des processus actifs.

1. Ouvrez un terminal et tapez `ps -ef`.
2. Identifiez les colonnes suivantes :
* **UID** : Utilisateur ayant lancé le processus.
* **PID** : L'identifiant unique du processus.
* **PPID** : Le PID du processus "Père".
* **C** ou **%CPU** : Utilisation du processeur.


3. Quel est le PID du tout premier processus lancé par le système (souvent `systemd` ou `init`) ? Quel est son PPID ?

---

## 2. Analyse dynamique : `top` et `htop`

1. Lancez la commande `top`. Elle se rafraîchit toutes les 3 secondes.
* Appuyez sur **M** pour trier par occupation mémoire (RAM).
* Appuyez sur **P** pour trier par occupation processeur (CPU).
* Quittez avec la touche **q**.


2. Lancez `htop` (plus visuel). Si la commande n'existe pas : `sudo apt install htop`.
* Combien de "cœurs" processeur votre machine possède-t-elle ?
* Quelle est la quantité de RAM actuellement utilisée ?



---

## 3. Création et observation d'un processus Python

Nous allons maintenant créer nos propres processus pour observer la relation Père/Fils.

### 📝 Le Script `famille.py`

Utilisez le script [`famille.py`](famille.py) :

### 🔍 Manipulation

1. Lancez le script dans un terminal : `python3 famille.py`.
2. **Laissez-le tourner** et ouvrez un **deuxième terminal**.
3. Tapez la commande de filtrage : `ps -ef | grep python3`.
* Combien de processus `python3` voyez-vous (excluez la ligne du `grep` lui-même) ?
* Vérifiez que le **PPID** du deuxième processus correspond bien au **PID** du premier.
* Expliquez le rôle du caractère "pipe" (`|`) dans cette commande.
* Recommencez en utilisant `htop`



---

## 4. Signaux et interruption

Lorsqu'un processus est bloqué ou trop gourmand, on peut lui envoyer des signaux.

1. Lancez une commande infinie en arrière-plan : `yes > /dev/null &`.
2. Trouvez son PID avec `ps` ou `top`.
3. Testez les commandes suivantes et observez le résultat (utilisez `htop` en parallèle) :
* `kill -STOP <PID>` : Met le processus en pause. Quel est son nouvel état dans `htop` ?
* `kill -CONT <PID>` : Relance le processus.
* `kill -9 <PID>` : Tue le processus immédiatement (Signal `SIGKILL`).


4. Tuez également vos processus Python lancés précédemment s'ils ne sont pas terminés.

---

## 5. Exercice de synthèse : La priorité (`nice`)

1. Lancez la commande `factor 99999999999999999999` (calcul de facteurs premiers). Observez l'usage CPU dans `htop`.
2. Relancez la même commande mais avec une priorité très basse :
`nice -n 15 factor 99999999999999999999 &`
3. Dans `htop`, repérez la colonne **NI** (Nice). Quelle est sa valeur ?
*Note : Plus la valeur Nice est haute, plus le processus est "gentil" et laisse la place aux autres.*

---

## À retenir :

* **PID** : Identifiant unique.
* **Ordonnancement** : Gestion du temps CPU entre les processus.
* **États** : Élu (Running), Prêt (Ready), Bloqué (Sleeping).
* **Interruption** : Utilisation de `kill`.

---

*Fin de l'énoncé.*