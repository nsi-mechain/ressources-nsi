#!/bin/bash

ORG="ciel-mechain"

echo "Que voulez-vous faire ?"
echo "1 - Créer les dépôts"
echo "2 - Supprimer les dépôts"
read -rp "Choix (1/2) : " CHOIX

case "$CHOIX" in
  1)
    for i in $(seq -w 1 10); do
      REPO="projet-$i"
      echo "Création de $REPO..."
      gh repo create "$ORG/$REPO" --public
    done
    ;;
  2)
    for i in $(seq -w 1 10); do
      REPO="projet-$i"
      echo "Suppression de $REPO..."
      gh repo delete "$ORG/$REPO" --yes
    done
    ;;
esac

