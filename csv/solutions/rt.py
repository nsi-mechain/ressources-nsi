import os

if not os.path.exists('t.txt'):
    print('Ce fichier n\'existe pas')
else:
    with open('t.txt', 'rt') as f:
        print(f.read())