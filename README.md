# 6GEI311 -- Laboratoire 2

## Système de gestion de tickets

### Membres de l'équipe

-   Cheikh Ahmadou Bamba Lo
-   Almamy Sylla

------------------------------------------------------------------------

## Présentation

Ce dépôt contient l'implémentation Python réalisée dans le cadre du
laboratoire 2 du cours **6GEI311 -- Architecture des logiciels**.

L'application permet de créer et de gérer des tickets et prend en charge
différents types de pièces jointes.

------------------------------------------------------------------------

## Installation

### Prérequis

-   Python 3

### Exécution

1.  Cloner ou télécharger le dépôt.
2.  Ouvrir le dossier du projet dans un terminal.
3.  Lancer le programme :

``` bash
python main.py
```

Aucune bibliothèque externe particulière n'est nécessaire.

------------------------------------------------------------------------

## Utilisation

Le programme principal propose des menus permettant d'utiliser les
fonctions associées aux utilisateurs et aux administrateurs.

### Fonctionnalités principales

**Utilisateur** - créer un ticket ; - consulter un ticket ; - modifier
certaines informations d'un ticket ; - ajouter des pièces jointes.

**Administrateur** - enregistrer et consulter les tickets ; - assigner
un ticket à un utilisateur ; - fermer un ticket ; - afficher les tickets
enregistrés.

**Pièces jointes** - fichiers texte ; - images ; - vidéos.

------------------------------------------------------------------------

## Organisation du projet

``` text
Projet/
├── main.py
├── User.py
├── Admin.py
├── Ticket.py
├── Attachment.py
├── README.md

```

-   `main.py` : point d'entrée du programme et menus.
-   `User.py` : opérations disponibles pour l'utilisateur.
-   `Admin.py` : opérations de gestion des tickets.
-   `Ticket.py` : données et opérations associées aux tickets.
-   `Attachment.py` : gestion des différents types de pièces jointes.

------------------------------------------------------------------------

## Diagrammes UML

### Partie 1 -- Diagramme initial

Diagramme UML initial

### Partie 2 -- Diagramme final

Diagramme UML final(voir rapport)

Les explications et les justifications des modifications apportées entre
les deux diagrammes sont présentées dans le **rapport du laboratoire**.

------------------------------------------------------------------------

## Résultats d'exécution

executer le code 

------------------------------------------------------------------------

## Apprentissages

Ce laboratoire nous a permis de mettre en pratique la conception et
l'implémentation d'une application orientée objet en Python. Nous avons
notamment travaillé sur la **modificabilité**, la répartition des
responsabilités entre les classes et l'utilisation de plusieurs types de
pièces jointes.

L'analyse détaillée des choix de conception et des améliorations
réalisées est présentée dans le rapport du laboratoire.
