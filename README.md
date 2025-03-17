# Jeu "3 pour 10"

## Aperçu
Le jeu "3 pour 10" est un jeu de placement de nombres amusant et captivant où les joueurs placent à tour de rôle des cartes numérotées de 1 à 8 sur un plateau. L'objectif est de placer stratégiquement les cartes pour former des combinaisons qui totalisent 10, marquant des points lorsque vous réussissez.

## Règles
- Les joueurs placent à tour de rôle des cartes numérotées de 1 à 8 sur le plateau.
- **Toutes les cartes sur le plateau comptent pour les deux joueurs** lors de la formation de combinaisons.
- Une combinaison se compose de 3 cartes qui totalisent exactement 10.
- Lorsqu'un joueur forme une combinaison (horizontale, verticale ou diagonale), il gagne un point.
- Une fois qu'une combinaison a été marquée dans une direction particulière, ces 3 cartes ne peuvent plus être utilisées pour marquer à nouveau dans la même direction.
- Chaque carte peut potentiellement faire partie de 4 combinaisons différentes : horizontale, verticale, diagonale montante et diagonale descendante.
- Le jeu se termine lorsque toutes les cartes sont placées ou qu'il n'y a plus de mouvements valides.
- Le joueur avec le score le plus élevé gagne.

## Implémentation de l'IA
Le jeu comprend un adversaire IA sophistiqué qui utilise une analyse basée sur des heuristiques pour prendre des décisions stratégiques. L'IA évalue les mouvements potentiels en utilisant plusieurs facteurs:

### Évaluation Heuristique
L'IA Intelligente utilise les critères d'évaluation suivants:
- **Marquage Immédiat:** L'IA privilégie les mouvements qui créent immédiatement des combinaisons gagnantes.
- **Potentiel Futur:** Elle analyse les positions qui pourraient conduire à des opportunités de marquage futures.
- **Blocage:** L'IA tente activement de bloquer les combinaisons potentielles du joueur humain.
- **Valeur Positionnelle:** Les positions centrales sont valorisées plus que les positions de bord, car elles offrent plus de possibilités de combinaisons.

### Processus de Prise de Décision
Pour chaque mouvement possible, l'IA:
1. Crée un état de jeu simulé
2. Évalue le mouvement en utilisant des facteurs de score pondérés
3. Sélectionne le mouvement avec le score global le plus élevé

Cette approche permet à l'IA de prendre des décisions intelligentes sans nécessiter des ressources computationnelles excessives, offrant un adversaire stimulant pour les joueurs humains.

## Fonctionnalités
- Architecture modulaire avec des classes distinctes pour la logique du jeu, les interactions des joueurs et la gestion du plateau.
- Support pour les joueurs humains et IA.
- Suivi des scores et gestion des tours.
- Adversaire IA stratégique avec prise de décision basée sur des heuristiques.

## Installation
Pour configurer le projet, clonez le dépôt et installez les dépendances requises:

```bash
git clone <repository-url>
cd three_for_ten_game
pip install -r requirements.txt
```

## Comment Jouer
1. Démarrez le jeu en exécutant le script principal:
   ```bash
   python src/main.py
   ```
2. Les joueurs placent à tour de rôle des cartes sur le plateau.
3. Le jeu continue jusqu'à ce que toutes les cartes soient placées ou qu'il n'y ait plus de mouvements valides.
4. Le joueur avec le score le plus élevé à la fin du jeu gagne.

## Structure du Répertoire
```
three_for_ten_game
├── src
│   ├── main.py
│   ├── game
│   │   ├── game.py
│   │   ├── board.py
│   │   └── card.py
│   ├── players
│   │   ├── player.py
│   │   ├── human_player.py
│   │   └── smart_ai_player.py
│   └── utils
│       └── constants.py
└── requirements.txt
```

