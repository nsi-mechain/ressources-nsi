_BTS CIEL Informatique et Réseaux_

# Mini-projet de fin d'année :

| Mini-projet    | Étudiant 1 | Étudiant 2 | Étudiant 3 |
| -------------- | ---------- | ---------- | ---------- |
| Mini projet 1  |            |            |            |
| Mini projet 2  |            |            |            |
| Mini projet 3  |            |            |            |
| Mini projet 4  |            |            |            |
| Mini projet 5  |            |            |            |
| Mini projet 6  |            |            |            |
| Mini projet 7  |            |            |            |
| Mini projet 8  |            |            |            |
| Mini projet 9  |            |            |            |
| Mini projet 10 |            |            |            |

## ***Objectifs***

- Mettre en œuvre un système fonctionnant en réseau
- Réaliser une application fonctionnant en temps réel

## ***Activités Professionnelles associées***

- Activité R2 : Installation et qualification***
- Activité R4 : Gestion de projet et d’équipe*** 
- Activité D2 : Développement et validation de solutions logicielles***

## ***Objectifs CIEL***

Le but de cette activité est de mobiliser les connaissances acquises en matière de développement logiciel et installation de systèmes tout en se préparant pour les épreuves du BTS CIEL.

Les compétences développées durant cette activité seront les suivantes :

- C01 :    COMMUNIQUER EN SITUATION PROFESSIONNELLE (FRANÇAIS/ANGLAIS)
- C03 :    GÉRER UN PROJET
- C04 :    ANALYSER UN SYSTÈME INFORMATIQUE
- C05 :    CONCEVOIR UN SYSTÈME INFORMATIQUE
- C06 :    VALIDER UN SYSTÈME INFORMATIQUE 
- C08 :    CODER

## ***Organisation***

- Le travail sera réalisé par 2 ou 3 étudiants. L’un d’entre eux assurera la tâche de *chef de projet* en plus de la partie qu’il aura à réaliser. La répartition des tâches est à sa charge.

- Le développement se fera sur 4 semaines.

- Les différentes parties sont :
  
  - Acquisition d'une grandeur physique par l'intermédiaire d'une carte à microcontrôleur
  - Traitement des données acquises
  - Installation des logiciels et Systèmes d'Exploitations :
    - Installation d'un client Windows
    - Installation d'un serveur Web sur un serveur Linux
    - Installation d'un serveur Windows configuré comme contrôleur de domaine et serveur DHCP
  - Archivage dans une BDD *Mariadb*
  - Diffusion d'informations sur le Web
  - Analyse des échanges d'informations

- L'ensemble des programmes et divers documents produits seront déposés sur **GitHub**, dans un dépôt nommé `ciel-mechain/projet-XX` (XX étant ne numéro du projet) organisé par le *chef de projet*.

## ***Présentation orale (avec diaporama)***

- Présentation de l’objectif global

- Présentation des objectifs des différentes parties

- Présentation des réalisations des différentes parties du projet

## ***Évaluation***

- Chaque étudiant sera évalué individuellement, à l’occasion des 10 min de l’exposé oral, mais aussi en tenant compte de la qualité des documents présentés.

- Une attention particulière sera portée au respect des points demandés dans le travail à réaliser.

# ■ Mini projet n° 01 :

## Contrôle de flux de visiteurs dans un musée

**Spécifications :**

Le système devra être capable d'effectuer un comptage du flux de personnes entrant et sortant d'un musée afin de déterminer en temps réel le nombre de personnes présentes et de faire des statistiques de fréquentation en fonction d'horaires.

**Matériel :**

- Raspberry Pi 400
- Carte Micro:bit
- Capteurs de personnes : simulés par les deux boutons de la Micro:bit

# ■ Mini projet n° 02 :

## Contrôle des paramètres d'une serre

**Spécifications :**

Le système devra être capable d'effectuer une mesure de température et d'humidité dans une serre horticole et d'assurer une ventilation automatique au delà de certains seuils.
Ces données atmosphériques et de ventilation devront être archivées dans une BDD et être consultables à distance

**Matériel :**

- Raspberry Pi 400
- Carte Arduino
- Capteur DHT22
- Ventilateur

# ■ Mini projet n° 03 :

## Gestion d'un éclairage automatique

**Spécifications :**

Le système devra être capable d'adapter l'éclairage d'une pièce en fonction de la luminosité naturelle : l'objectif est de compenser une baisse de luminosité
par un éclairage à LEDS. Il faudra archiver la mesure de luminosité et l'énergie consommée par l'éclairage afin de pouvoir faire des statistiques en fonction d'horaires.

**Matériel :**

- Raspberry Pi 400
- Carte Micro:bit
- Capteurs de luminosité : LEDS de la Micro:bit
- Actionneurs : 4 LEDS de puissance interfacée par MOS-FET

# ■ Mini projet n° 04 :

## Contrôle de la vitesse d'un coureur

**Spécifications :**

Le système devra être capable d'acquérir la vitesse instantanée d'un coureur sur 400 m et de l'afficher en temps réel.
Les données seront archivées dans une BDD en vue de tracer les courbes de vitesse qui seront accessibles à distance.

**Matériel :**

- Raspberry Pi 400
- Carte Arduino
- Capteur : module GPS + transmetteur radio
- Actionneur : indicateur à aiguille

# ■ Mini projet n° 05 :

## Contrôle d'accès par QR Code

**Spécifications :**

Le système devra être capable de lire un QR Code et d'autoriser l'accès à un local. Les données seront archivées dans une BDD et seront accessibles à distance.

**Matériel :**

- Raspberry Pi 400
- Raspberry Pi 4
- Capteur : Caméra
- Actionneur : Carte Relais

# ■ Mini projet n° 06 :

## Contrôle d'un générateur de sons

**Spécifications :**

Le système devra être capable de générer un son en fonction de la position des mains. Les séquences sonores seront archivées dans une BDD et seront accessibles à distance.

**Matériel :**

- Raspberry Pi 400
- Arduino
- Capteur : Capteurs ultrason SR04

# ■ Mini projet n° 07 :

## Contrôle d'un affichage de Température et luminosité sur un afficheur Led

**Spécifications :**

Le système devra être capable de capter la température et la luminosité ambiante. Les données seront archivées dans une BDD et seront accessibles à distance.

**Matériel :**

- Raspberry Pi 400
- Arduino
- Capteur : Capteurs CTN et photorésistance
- Actionneur : Afficheur Led

# ■ Mini projet n° 08 :

## Suivi de consommation électrique d'une installation autonome

**Spécifications :**

Le système devra être capable de mesurer la tension et le courant prélevé sur une batterie d'une installation autonome. En temps réel on affichera la puissance consommée sur un afficheur à leds. Les données seront archivées dans une BDD et seront accessibles à distance.

**Matériel :**

- Raspberry Pi 400
- Arduino
- Capteur : résistance
- Actionneur : Afficheur RGB Led WS2812B

# ■ Mini projet n° 09 :

## Contrôle d'un affichage de poids à l'aide d'un capteur de force

**Spécifications :**

Le système devra être capable de mesurer un poids à l'aide d'un capteur de force. Les données seront affichées sur un afficheur 7 segments et archivées dans une BDD pour être accessibles à distance.

**Matériel :**

- Raspberry Pi 400
- Arduino
- Capteur : Capteur de Force
- Actionneur : Afficheur 7 segments

# ■ Mini projet n° 10 :

## Contrôle de la température d'une pièce et affichage sur un afficheur LCD

**Spécifications :**

Le système devra être capable de capter la température d'une pièce. Les données seront affichées sur un afficheur LCD et archivées dans une BDD pour être accessibles à distance.

**Matériel :**

- Raspberry Pi 400
- Arduino
- Capteur : Capteur de température I2C
- Actionneur : Afficheur LCD I2C
