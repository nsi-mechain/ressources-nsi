![Static Badge](https://img.shields.io/badge/Notice-green?logo=github&logoColor=white&label=GitHub)

# Utiliser GitHub sur deux postes de travail (ou plus)

## Objectif

Travailler sur un même dépôt GitHub depuis le PC du lycée **et** votre ordinateur personnel, sans jamais perdre de modifications.

---

## Rappel important

Votre dépôt GitHub est le **point central**. Chaque poste de travail possède une copie locale du dépôt.

---

## Routine à suivre sur chaque poste de travail

### 1. Avant de commencer à travailler

Pour récupérer la version la plus récente du dépôt :

```bash
git pull
```

---

### 2. Après avoir travaillé (ajouts, modifications…)

Enregistrez vos modifications localement :

```bash
git add --all
git commit -m "Votre message de commit"
```

---

### 3. À la fin de la session de travail

Envoyez vos modifications vers GitHub :

```bash
git push
```

---

### 4. Quand vous changez de poste

1. Sur le nouveau poste, commencez toujours par :
   
   ```bash
   git pull
   ```

2. Travaillez normalement (modifiez, ajoutez, supprimez, commit…).

3. Terminez par :
   
   ```bash
   git push
   ```

---

## Conseils pratiques

- En cas de message d’erreur ou de conflit, lisez attentivement l’explication ou demandez de l’aide.
- Faites des *commits* réguliers avec des messages explicites.
- Ne supprimez **jamais** le dossier `.git` dans le dépôt !
- Faites régulièrement une sauvegarde de l'ensemble de votre dépôt sur un autre support (clé USB).

---

## Interface graphique

Pour plus de facilité, vous pourrez ensuite utiliser une interface graphique (mais c'est un peu lent sur *Raspberry Pi*, préférez [Git-Cola](https://git-cola.github.io/))

- GUI **Git/GitHub**
  - pour *Windows* : [Github Desktop](https://github.com/apps/desktop)
  - pour *Linux* : [GitHub Desktop - The Linux Fork](https://github.com/shiftkey/desktop)

---

**Respecter cette routine, c’est garantir la cohérence et la sécurité de votre travail partout.**
