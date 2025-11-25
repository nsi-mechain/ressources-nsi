# Fiches corrigés des sujets 03 et 04

## 🔵 PDF des sujets et corrigés des exercices :

- https://github.com/nsi-mechain/ressources-nsi/tree/main/bdd/sujets_bac/sujet03
- https://github.com/nsi-mechain/ressources-nsi/tree/main/bdd/sujets_bac/sujet04

## 🔵 Vous établirez deux fichiers *Markdown* à déposer dans votre dépôt *GitHub* :

- fiche-sujet-03.md
- fiche-sujet-04.md

## 🔵 Ces "fiches-corrigé" contiendront :

### ▶ Le code SQL de création de la BDD

- Utilisez le formatage *Markdown* approprié pour obtenir une coloration syntaxique comme :

    ```sql
    CREATE TABLE matable
	(Id INT ...)
    ```

### ▶ Les sorties des commandes internes *sqlite3* `.tables` et `.schéma`

- Vous utiliserez *sqlite3* en ligne de commande pour créer votre BDD et copierez la sortie dans un bloc comme :

	```
	sqlite> .tables
	AUTEURS  LIVRES 
	sqlite> .schema
	CREATE TABLE AUTEURS
	(id INT, nom TEXT, prenom TEXT, ann_naissance INT, langue_ecriture TEXT, PRIMARY KEY (id));
	...
	sqlite>
	```
### ▶ La représentation graphique de la BDD

- Utilisez https://drawdb.vercel.app
- Faites un export *mermaid* (correctement interprété par *GitHub* ainsi que par *VSCodium* avec l'extension **Mermaid Chart**)

### ▶ Le contenu de toutes les tables (après les avoir remplies avec l'outil de votre choix)

- Utilisez des requêtes `SELECT ...` et la commande `.mode markdown` ) pour obtenir un formatage sous forme de table *Markdown* :

	| id |   nom    |    prenom    | ann_naissance | langue_ecriture |
	|----|----------|--------------|---------------|-----------------|
	| 1  | Orwell   | George       | 1903          | anglais         |
	| 2  | Herbert  | Frank        | 1920          | anglais         |
	| 3  | Asimov   | Isaac        | 1920          | anglais         |


### ▶ Toutes les requêtes SQL du sujet, **dans l'ordre** des questions, avec les résultats **probants**

- Codes SQL avec coloration syntaxique
- Mode markdown dans *sqlite3* pour les résultats des requêtes

---