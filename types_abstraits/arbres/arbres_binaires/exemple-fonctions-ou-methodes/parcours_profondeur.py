def parcours_profondeur(arbre, type='prefixe'):
    if arbre is None:
        return []

    if type == 'prefixe':
        return [arbre['valeur']] + parcours_profondeur(arbre['gauche'], type) + parcours_profondeur(arbre['droit'], type)
    elif type == 'infixe':
        return parcours_profondeur(arbre['gauche'], type) + [arbre['valeur']] + parcours_profondeur(arbre['droit'], type)
    elif type == 'postfixe':
        return parcours_profondeur(arbre['gauche'], type) + parcours_profondeur(arbre['droit'], type) + [arbre['valeur']]
    else:
        raise ValueError("Type de parcours invalide. Utilisez 'prefixe', 'infixe' ou 'postfixe'.")


arbre_exemple = {
    'valeur': 1,
    'gauche': {
        'valeur': 2,
        'gauche': None,
        'droit': None
    },
    'droit': {
        'valeur': 3,
        'gauche': None,
        'droit': None
    }
}

print(parcours_profondeur(arbre_exemple, 'prefixe'))  # [1, 2, 3]
print(parcours_profondeur(arbre_exemple, 'infixe'))   # [2, 1, 3]
print(parcours_profondeur(arbre_exemple, 'postfixe')) # [2, 3, 1]
