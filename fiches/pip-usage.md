![Static Badge](https://img.shields.io/badge/Conseils-green?logo=python&logoColor=yellow&label=pip)

# Mémo PIP

## Installation / Mise à jour

| Commande                              | Utilité                    |
| ------------------------------------- | -------------------------- |
| `pip install <package>`               | Installer un paquet        |
| `pip install --upgrade <package>`     | Mettre à jour un paquet    |
| `pip uninstall <package>`             | Désinstaller un paquet     |
| `python -m pip install --upgrade pip` | Mettre à jour pip lui-même |

---

## Gestion des paquets

| Commande                          | Utilité                                  |
| --------------------------------- | ---------------------------------------- |
| `pip list`                        | Lister tous les paquets installés        |
| `pip list --outdated`             | Afficher les paquets à mettre à jour     |
| `pip show <package>`              | Informations sur un paquet               |
| `pip freeze`                      | Exporter les paquets (pour requirements) |
| `pip install -r requirements.txt` | Installer tous les paquets listés        |

---

## Astuces pratiques

- **Lister et mettre à jour tous les paquets :**
  
  Installer `pip-review` puis :
  
  ```python
  pip-review --auto
  ```

- **Générer un fichier requirements.txt :**
  
  ```bash
  pip freeze > requirements.txt
  ```

---

## Rappels

- Activez toujours votre environnement virtuel (`venv`) avant d’utiliser pip dans un projet !
- Privilégiez la commande : `python -m pip ...` pour éviter les conflits de version.

---
