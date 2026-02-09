# Fiche mémo : Markdown standard & GitHub Flavored Markdown (GFM)

## 🔹 Markdown standard

### Titres
```markdown
# Titre 1
## Titre 2
### Titre 3
```

### Texte
- **Gras** : `**texte**` → **texte**  
- *Italique* : `*texte*` → *texte*  
- ~~Barré~~ : `~~texte~~` → ~~texte~~  
- `Code inline` : `` `code` `` → `code`

### Listes
- Liste à puces :
```markdown
- élément 1
- élément 2
```
- Liste numérotée :
```markdown
1. premier
2. deuxième
```

### Liens et images
```markdown
[OpenAI](https://openai.com)
![Logo](image.png)
```

### Citations
```markdown
> Ceci est une citation
```
> Ceci est une citation

### Blocs de code
````markdown
```python
print("Hello World")
```
````

### Tableaux simples
```markdown
| Colonne 1 | Colonne 2 |
|-----------|-----------|
| valeur A  | valeur B  |
```

| Colonne 1 | Colonne 2 |
|-----------|-----------|
| valeur A  | valeur B  |

### Séparateur
```markdown
---
```
---

## 🔹 GitHub Flavored Markdown (GFM)

### ✅ Listes de tâches
```markdown
- [x] Tâche faite
- [ ] Tâche à faire
```
- [x] Tâche faite
- [ ] Tâche à faire

### 👤 Mentions & références
- `@utilisateur` → mentionner une personne  
- `#123` → référence à un *issue* ou *pull request*  
- `:emoji:` → 😃

### 💻 Code avec coloration
````markdown
```python
def hello():
    print("Hello GitHub")
```
````

### 📊 Tableaux enrichis
```markdown
| Nom   | Âge |
|-------|-----|
| Alice | 20  |
| Bob   | 22  |
```

| Nom   | Âge |
|-------|-----|
| Alice | 20  |
| Bob   | 22  |

### 🔗 Liens automatiques
```
https://github.com
```
→ https://github.com

### ❌ Barré
```markdown
~~texte~~
```
→ ~~texte~~

---

✍️ **Astuce** : GFM = Markdown standard + fonctionnalités spécifiques à GitHub.
