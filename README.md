# Three for Ten Game

## Overview
The "3 for 10" game is a fun and engaging number placement game where players take turns placing cards numbered from 1 to 8 on a board. The objective is to strategically place cards to maximize your score while minimizing your opponent's opportunities.

## Features
- Modular architecture with separate classes for game logic, player interactions, and board management.
- Support for both human and AI players.
- Score tracking and turn management.

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