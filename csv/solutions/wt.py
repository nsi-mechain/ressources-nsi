import os

if os.path.exists('t.txt'):
    print('Ce fichier existe déjà')
else:
    with open('t.txt', 'wt') as f:
        f.write(input('Entrez votre ligne de texte : '))