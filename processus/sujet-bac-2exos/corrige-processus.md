# Corrigé — Exercices sur la gestion des processus

---

## EXERCICE 2 — Premier sujet

### Partie A — QCM

| Question | Réponse | Justification |
|----------|---------|---------------|
| 1 | **b. `ps`** | `ps` (Process Status) affiche les processus en cours d'exécution sous UNIX |
| 2 | **c. PID** | PID = *Process Identifier*, identifiant unique d'un processus |
| 3 | **b. L'ordonnancement** | L'ordonnancement (*scheduling*) gère le partage du processeur entre les processus |
| 4 | **d. `kill`** | La commande `kill` envoie un signal à un processus pour l'interrompre |

---

### Partie B

#### Question 1 — Ordonnancement par priorité

Rappel des données :

| Processus | Durée | Arrivée | Priorité |
|-----------|-------|---------|----------|
| P1 | 3 | 3 | 1 (plus haute) |
| P2 | 3 | 2 | 2 |
| P3 | 4 | 0 | 3 (plus basse) |

**Règle :** à chaque cycle, le processus **présent** avec le **plus petit numéro de priorité** est exécuté (préemptif).

**Déroulement cycle par cycle :**

- **Cycle 0** → seul P3 est arrivé → **P3**
- **Cycle 1** → seul P3 est présent → **P3**
- **Cycle 2** → P2 arrive (priorité 2 < 3) → P3 suspendu → **P2**
- **Cycle 3** → P1 arrive (priorité 1 < 2) → P2 suspendu → **P1**
- **Cycle 4** → P1 (prio 1) toujours le plus prioritaire → **P1**
- **Cycle 5** → P1 termine → P2 reprend (prio 2) → **P2**
- **Cycle 6** → **P2**
- **Cycle 7** → P2 termine → P3 reprend (prio 3) → **P3**
- **Cycle 8** → **P3**
- **Cycle 9** → P3 termine

**Tableau de Gantt :**

| Cycle | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|-------|---|---|---|---|---|---|---|---|---|
| Processus | P3 | P3 | P2 | P1 | P1 | P1 | P2 | P2 | P3 |

> P3 s'exécute aux cycles 0, 1, 7, 8 (4 cycles au total ✓)  
> P2 s'exécute aux cycles 2, 5, 6 (3 cycles ✓)  
> P1 s'exécute aux cycles 3, 4, ... → P1 dure 3 cycles : 3, 4, 5 ✓

*(Correction : P1 s'exécute cycles 3-4-5, P2 reprend cycles 6-7-8... recalcul ci-dessous)*

**Tableau corrigé détaillé :**

| Cycle | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|-------|---|---|---|---|---|---|---|---|---|---|
| Processus | P3 | P3 | P2 | P1 | P1 | P1 | P2 | P2 | P3 | P3 |

---

#### Question 2 — Interblocage

**Analyse des scénarios :**

**Scénario 1 :**
1. P1 acquiert R1, P2 acquiert R2
2. P3 attend R1 (P1 la détient)
3. P2 **libère** R2 → P3 n'est plus bloqué sur R2
4. P2 attend R1 → mais P1 **libère** R1 ensuite

→ **Pas d'interblocage** : P1 libère R1, ce qui débloque P2 et P3.

---

**Scénario 2 :**
1. P1 acquiert R1, P2 acquiert R3, P3 acquiert R2
2. P1 attend R2 (détenue par P3), P3 attend R1 (détenue par P1)
3. P2 libère R3, puis attend R1

→ **Interblocage entre P1 et P3** :
- P1 détient R1 et attend R2
- P3 détient R2 et attend R1
- Chacun attend une ressource détenue par l'autre → **cycle d'attente sans issue**

✅ **C'est le Scénario 2 qui provoque un interblocage.**

---

**Scénario 3 :**
1. P1 acquiert R1, P2 acquiert R2
2. P3 attend R2 (détenue par P2), P1 attend R2 (détenue par P2)
3. P2 **libère** R2 → P3 acquiert R2

→ **Pas d'interblocage** : P2 libère R2, ce qui débloque les processus en attente.

---

## EXERCICE 2 — Deuxième sujet

### Question 1 — Arborescence UNIX

L'arborescence de `/home/morgane` contient : `lycee/` (avec `francais/` et `NSI/` qui contient `info.txt` et `image1.jpg`) et `perso/`.

**(a) Résultat de `ls` depuis `/home/morgane` :**

> **Proposition 2 : `lycee perso`**  
> `ls` n'affiche que le contenu direct du répertoire courant (pas récursif).

**(b) Commande pour atteindre `lycee` depuis `/home/morgane` :**

```bash
cd lycee
```

**(c) Créer le répertoire `algorithmique` depuis `/home/morgane/lycee/NSI` :**

```bash
mkdir algorithmique
```

**(d) Supprimer `image1.jpg` depuis `/home/morgane/lycee/NSI` :**

```bash
rm image1.jpg
```

---

### Question 2 — Lecture de `ps`

**(a) PID du parent du processus `vi` :**

Le processus `vi` a le PID **1153** et le PPID **927**.  
→ Le PID du parent est **927** (processus `bash`).

**(b) PID d'un enfant du processus `xfce4-terminal` (PID 923) :**

Les processus dont le PPID est 923 : **1058** (`bash`) et **1155** (`ps -aef`).  
→ Par exemple **1058**.

**(c) Deux processus ayant le même parent :**

- PID **918** et PID **919** ont tous deux le PPID **823**
- (ou PID **1153** et PID **1154** avec PPID **927**, ou PID **1058** et **1155** avec PPID **923**)

**(d) Les deux processus ayant consommé le plus de temps processeur :**

La colonne TIME indique `00:00:02` pour deux processus :
- PID **923** (`xfce4-terminal`)
- PID **1036** (`mousepad`)

→ Ce sont les PIDs **923** et **1036**.

---

### Question 3 — Ordonnancement (P1=3, P2=1, P3=4, arrivée à t=0)

**(a) Tourniquet (quantum = 1 unité de temps) — file initiale : P1, P2, P3**

Déroulement (rotation circulaire) :

| t | 0→1 | 1→2 | 2→3 | 3→4 | 4→5 | 5→6 | 6→7 | 7→8 |
|---|-----|-----|-----|-----|-----|-----|-----|-----|
| Exécuté | P1 | P2 | P3 | P1 | P3 | P1 | P3 | P3 |

> P2 (durée 1) termine dès t=2. P1 (durée 3) termine à t=6. P3 (durée 4) termine à t=8.

**(b) Plus court d'abord (SJF non préemptif) — ordre croissant : P2(1), P1(3), P3(4)**

| t | 0→1 | 1→2 | 2→3 | 3→4 | 4→5 | 5→6 | 6→7 | 7→8 |
|---|-----|-----|-----|-----|-----|-----|-----|-----|
| Exécuté | P2 | P1 | P1 | P1 | P3 | P3 | P3 | P3 |

---

### Question 4 — Interblocage avec R1, R2, R3

Les files d'exécution :

| P1 | P2 | P3 |
|----|----|----|
| Demande R1 | Demande R2 | Demande R3 |
| Demande R2 | Demande R3 | Demande R1 |
| Libère R1 | Libère R2 | Libère R3 |
| Libère R2 | Libère R3 | Libère R1 |

**(a) États d'un processus et risque d'interblocage**

Les trois états d'un processus sont :
- **Prêt** (*ready*) : le processus attend d'être sélectionné par l'ordonnanceur
- **En exécution** (*running*) : le processus utilise le processeur
- **Bloqué** (*waiting*) : le processus attend la disponibilité d'une ressource

**Ordre d'exécution provoquant un interblocage :**

```
P1 demande R1  → obtient R1
P2 demande R2  → obtient R2
P3 demande R3  → obtient R3
P1 demande R2  → bloqué (R2 détenu par P2)
P2 demande R3  → bloqué (R3 détenu par P3)
P3 demande R1  → bloqué (R1 détenu par P1)
```

Cycle : P1 → attend R2 → P2 → attend R3 → P3 → attend R1 → P1 : **interblocage circulaire**.

**(b) Ordre d'exécution sans interblocage**

Il suffit qu'un processus termine avant que le cycle se forme :

```
P1 demande R1  → obtient R1
P1 demande R2  → obtient R2
P1 libère R1
P1 libère R2
P2 demande R2  → obtient R2
P2 demande R3  → obtient R3
P2 libère R2
P2 libère R3
P3 demande R3  → obtient R3
P3 demande R1  → obtient R1
P3 libère R3
P3 libère R1
```

Exécution séquentielle complète de chaque processus : pas de concurrence → pas d'interblocage possible.
