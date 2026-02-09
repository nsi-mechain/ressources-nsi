#! /bin/bash

# 1. Supprimez l’historique git local
rm -rf .git

# 2. Réinitialisez le dépôt git local
git init

# 3. Ajoutez tous les fichiers à l’index
git add .

# 4. Créez un commit unique
git commit -m "Dépôt nettoyé"

# 5. Renommez la branche en 'main' (optionnel mais recommandé)
git branch -m main

# 6. Ajoutez le dépôt distant en SSH (remplacez si besoin)
git remote add origin git@github.com:nsi-mechain/ressources-nsi.git

# 7. Vérifiez l’URL du dépôt distant
git remote -v

# 8. Forcer l’envoi de la nouvelle branche 'main' sur GitHub
git push --force --set-upstream origin main

