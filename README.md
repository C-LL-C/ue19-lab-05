# ue19-lab-05 - Application Python de Blagues

[![Python Version](https://img.shields.io/badge/python-3.x-blue.svg)](https://www.python.org/)
[![Docker](https://img.shields.io/badge/docker-available-blue.svg)](https://www.docker.com/)

## Description

Ce projet est une application Python 3 qui interroge un service API public, **JokesAPI**, pour récupérer une blague aléatoire et l'afficher à l'utilisateur.

L'application utilise la librairie `requests` pour envoyer une requête à l'API, obtenir une blague et l'afficher dans la console.

## Fonctionnalités

- Envoi de requêtes GET à l'API **JokesAPI** pour obtenir une blague.
- Affichage de la blague dans la console.
- Gestion des erreurs si la requête échoue ou si aucune blague n'est trouvée.

## Prérequis

Avant d'exécuter l'application, assurez-vous que votre système dispose des éléments suivants :

- Python 3.x
- pip (pour installer les dépendances)
- Docker (si vous préférez exécuter l'application dans un conteneur Docker)

## Installation

1. **Clonez le repository** :

   ```bash
   git clone https://github.com/C-LL-C/ue19-lab-05.git
   cd ue19-lab-05
