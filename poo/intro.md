# POOL

## Cours :

Voir la page de [Lyceum](https://www.lyceum.fr/tg/nsi/1-structures-de-donnees/2-programmation-objet/), ainsi que le Quizz et les exercices proposés.

## Exercices :

1. Dans un REPL, créez une classe `C` sans attribut ni méthode, puis instanciez deux objets référencés `ob1` et `ob2`.
   - Affichez les adresses mémoire de ces deux objets.
   - Utilisez le mot clé `del` pour **détruire** `ob1`.
   - Référencez `ob2` par un identifiant `ob3`, puis montrez que `ob2` et `ob3` sont bien des références du même objet par deux méthodes différentes.
   - Faites en sorte que l’identifiant `ob3` ne référence plus rien (sans pour autant détruire cet identifiant), puis prouvez-le.
   - Détruisez `ob3`, puis prouvez qu’il n’existe plus.

2. Dans votre IDE préféré, créez une classe `Chat` avec trois attributs (nom, sexe et masse) et leurs trois accesseurs (“getters”), et deux méthodes (`grossir` et `maigrir`).
   - Instanciez deux chats :
     - `chat1` : minou, un chat de 5kg
     - `chat2` : minette, une chatte de 4 kg
   - Vérifiez que minou est plus lourd que minette, et qu’ils sont de sexe différents.
   - Faites grossir `minou` de 200g et maigrir `minette` de 150g, puis affichez leurs masses.
   - Ajoutez à `Chat` la méthode prédéfinie `__str__` pour que `print(nom)` affiche “minou est un mâle de 5.2kg” ou “minette est une femelle de 3.85kg”.
   - Surchargez l’opérateur `+` pour faire naître `mina` (qui sera femelle par défaut et pèsera [100g](https://matou-miaou.com/poids-chaton/)).
   - Laissez-la téter jusqu’à ce qu’elle grossisse de 600g, puis affichez-la avec `print`.
   - Écrabouillez les parents, puis prouvez qu’ils sont bien morts.
