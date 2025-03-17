# Three for Ten Game

## Overview
The "3 for Ten" game is a fun and engaging number placement game where players take turns placing cards numbered from 1 to 8 on a board. The objective is to strategically place cards to form combinations that sum to 10, scoring points when successful.

## Rules
- Players take turns placing cards numbered 1-8 on the board.
- **All cards on the board count for both players** when forming combinations.
- A combination consists of 3 cards that sum to exactly 10.
- When a player forms a combination (horizontal, vertical, or diagonal), they earn a point.
- Once a combination has been scored in a particular direction, those 3 cards cannot be used to score again in the same direction.
- Each card can potentially be part of 4 different combinations: horizontal, vertical, diagonal up, and diagonal down.
- The game ends when all cards are placed or no valid moves are left.
- The player with the highest score wins.

## AI Implementation
The game includes a sophisticated AI opponent that uses heuristic-based analysis to make strategic decisions. The AI evaluates potential moves using several factors:

### Heuristic Evaluation
The SmartAI uses the following evaluation criteria:
- **Immediate Scoring:** The AI prioritizes moves that create scoring combinations immediately.
- **Future Potential:** It analyzes positions that could lead to future scoring opportunities.
- **Blocking:** The AI actively tries to block the human player's potential scoring combinations.
- **Positional Value:** Central positions are valued higher than edge positions, as they offer more combination possibilities.

### Decision-Making Process
For each possible move, the AI:
1. Creates a simulated game state
2. Evaluates the move using weighted scoring factors
3. Selects the move with the highest overall score

This approach allows the AI to make intelligent decisions without requiring excessive computational resources, providing a challenging opponent for human players.

## Features
- Modular architecture with separate classes for game logic, player interactions, and board management.
- Support for both human and AI players.
- Score tracking and turn management.
- Strategic AI opponent with heuristic-based decision making.

## Installation
To set up the project, clone the repository and install the required dependencies:

```bash
git clone <repository-url>
cd three_for_ten_game
pip install -r requirements.txt
```

## How to Play
1. Start the game by running the main script:
   ```bash
   python src/main.py
   ```
2. Players take turns placing cards on the board.
3. The game continues until all cards are placed or no valid moves are left.
4. The player with the highest score at the end of the game wins.

## Directory Structure
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
│   │   └── ai_player.py
│   └── utils
│       └── constants.py
├── tests
│   ├── test_game.py
│   └── test_player.py
└── requirements.txt
```

## Contributing
Contributions are welcome! Please submit a pull request or open an issue for any suggestions or improvements.

## License
This project is licensed under the MIT License. See the LICENSE file for details.