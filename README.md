# 🎰 Blackjack Casino Game 🃏

![Blackjack Logo](https://img.shields.io/badge/Blackjack-Casino-red?style=for-the-badge)
[![Python](https://img.shields.io/badge/Python-3.6+-blue?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)

## 📜 Overview

Welcome to the ultimate Python Blackjack experience! This casino-style implementation brings the excitement of Las Vegas directly to your terminal. Challenge the dealer, place your bets, and test your luck and strategy in this classic card game.

## ✨ Features

- 🎮 Full Blackjack game implementation with realistic rules
- 💰 Chip-based betting system (1K, 3K, 5K, 10K denominations)
- 🎯 Score calculation with special handling for Aces and Blackjacks
- 🏆 Win/lose conditions with appropriate messages
- 💵 Persistent chip tracking throughout gaming sessions
- 🔄 Auto-refill of chips when balance falls below minimum threshold

## 🎲 Game Rules

- 🎴 Goal: Get closer to 21 than the dealer without going over
- 🃏 Card values:
  - Number cards (2-10): Face value
  - Face cards (J, Q, K): 10 points
  - Ace: 11 points or 1 point (automatically adjusts to prevent busting)
- 💯 Blackjack: An Ace with a 10, J, Q, or K (first two cards totaling 21)
- 🤖 Dealer must draw until reaching at least 17 points
- 💸 Win with Blackjack or by having a higher score than the dealer without busting

## 🚀 Getting Started

### Prerequisites

- Python 3.6 or higher
- [`art`](https://pypi.org/project/art/) package for ASCII art logo

### Installation

1. Clone the repository:

```bash
git clone https://github.com/JeremyPanggabean/Blackjack-Games.git
```

2. Change the directory:

```bash
cd Blackjack-Games
```

3. Install required packages:

```bash
pip install art
```

4. Run the game:

```bash
python blackjack_program.py
```

## 🎮 How to Play

1. Start the game by typing `y` when prompted
2. Choose your bet amount from available chip denominations
3. Decide whether to "hit" (get another card) or "stand" (keep current hand)
4. Try to beat the dealer without going over 21
5. Watch your chip balance grow as you win!

## 📋 Code Structure

- `deal_card()`: Randomly selects cards from the deck
- `calculate_score()`: Handles scoring logic including Ace values and Blackjack detection
- `compare()`: Determines the winner based on final hand values
- `format_chips()`: Formats chip amounts with appropriate separators
- `play_game()`: Main game loop handling betting, card dealing, and result calculation

## 🖼️ Preview

```
Do you want to play a game of Blackjack? Type 'y' or 'n': y


.------.            _     _            _    _            _
|A_  _ |.          | |   | |          | |  (_)          | |
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   <
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |
      `------'                           |__/

You have 10.000 chips.
Available chip bets: ['1K', '3K', '5K', '10K']
Choose your bet (1K, 3K, 5K, 10K): 3K
Your cards: [8, 9], current score: 17
Computer's first card: 8
Type 'y' to get another card, type 'n' to pass: n
Your final hand: [8, 9], final score: 17
Computer's final hand: [8, 7, 4], final score: 19
You lose 😌
You now have 7.000 chips.
Do you want to play a game of Blackjack? Type 'y' or 'n': y


.------.            _     _            _    _            _
|A_  _ |.          | |   | |          | |  (_)          | |
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   <
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |
      `------'                           |__/

You have 7.000 chips.
Available chip bets: ['1K', '3K', '5K', '10K']
Choose your bet (1K, 3K, 5K, 10K): 5K
Your cards: [10, 2], current score: 12
Computer's first card: 2
Type 'y' to get another card, type 'n' to pass: y
Your cards: [10, 2, 10], current score: 22
Computer's first card: 2
Your final hand: [10, 2, 10], final score: 22
Computer's final hand: [2, 10, 1, 8], final score: 21
You busted! You lose 😭
You now have 2.000 chips.
Do you want to play a game of Blackjack? Type 'y' or 'n': y


.------.            _     _            _    _            _
|A_  _ |.          | |   | |          | |  (_)          | |
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   <
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |
      `------'                           |__/

You have 2.000 chips.
Available chip bets: ['1K', '3K', '5K', '10K']
Choose your bet (1K, 3K, 5K, 10K): 1K
Your cards: [5, 10], current score: 15
Computer's first card: 10
Type 'y' to get another card, type 'n' to pass: n
Your final hand: [5, 10], final score: 15
Computer's final hand: [10, 4, 10], final score: 24
Computer busted! You win 🤩
You now have 3.000 chips.
Do you want to play a game of Blackjack? Type 'y' or 'n': y


.------.            _     _            _    _            _
|A_  _ |.          | |   | |          | |  (_)          | |
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   <
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |
      `------'                           |__/

You have 3.000 chips.
Available chip bets: ['1K', '3K', '5K', '10K']
Choose your bet (1K, 3K, 5K, 10K): 3K
Your cards: [5, 4], current score: 9
Computer's first card: 10
Your final hand: [5, 4], final score: 9
Computer's final hand: [10, 11], final score: 0
Lose, Computer has a Blackjack 😮
You now have 3.000 chips.
Do you want to play a game of Blackjack? Type 'y' or 'n': n
Thank you for playing Blackjack! 🎉
```

## 🤝 Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgements

- Inspired by classic casino Blackjack games
- ASCII art logo generated with the `art` package
- Built with love for card game enthusiasts

---

⭐️ Star this repository if you found it useful! ⭐️
