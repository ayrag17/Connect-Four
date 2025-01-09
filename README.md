# Connect Four

A customizable Python implementation of the classic "Connect Four" game, where two players compete to get four of their pieces in a row, either horizontally, vertically, or diagonally. The game features both human vs. human and human vs. AI gameplay.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Game Rules](#game-rules)
- [Classes](#classes)
- [AI Player](#ai-player)
- [License](#license)

## Overview

This project implements a customizable version of the popular **Connect Four** game. The game can be played in a terminal, and players can customize the board size. The game supports both two-player (human vs. human) and human vs. AI gameplay.

- **Customizable Board Size**: The board's dimensions are configurable (e.g., you can have a 7x6 board, a 10x8 board, or any other size).
- **AI Player**: Includes an AI opponent that uses lookahead to evaluate the best move.

## Features

- Customizable board dimensions.
- Two-player gameplay (human vs. human).
- Human vs. AI gameplay (AI makes moves using a lookahead strategy).
- Simple text-based interface in the terminal/console.
- Check for a winner (horizontal, vertical, and diagonal).
- Game board display after every move.
- Easy-to-understand game rules.

## Game Rules

1. **Players**: The game is for two players. Player 1 uses "X" and Player 2 uses "O".
2. **Objective**: Players take turns dropping their discs into a column. The goal is to get four of their discs in a row (vertically, horizontally, or diagonally).
3. **Turn Order**: Players alternate turns, and each disc is placed at the lowest available space in the chosen column.
4. **Winning**: A player wins by connecting four of their discs in a row, either horizontally, vertically, or diagonally.
5. **Draw**: If the board fills up without a player connecting four discs, the game ends in a draw.

## Classes

This game is structured using the following classes:

### 1. `Board`
   - **Purpose**: Represents the game board and manages the placement of discs.
   - **Key Methods**:
     - `display()`: Prints the current state of the board to the console.
     - `is_full()`: Checks if the board is full.
     - `drop_disc(column, player)`: Drops the player's disc into the specified column.
     - `check_winner()`: Checks if there is a winner by analyzing horizontal, vertical, and diagonal lines.

### 2. `Game`
   - **Purpose**: Manages the game flow, including player turns, winning conditions, and input validation.
   - **Key Methods**:
     - `play()`: Starts the game and handles the turn sequence.
     - `switch_player()`: Switches between Player 1 and Player 2.

### 3. `Player`
   - **Purpose**: Represents a player in the game.
   - **Key Attributes**:
     - `symbol`: The symbol representing the player ('X' or 'O').
     - `name`: The player's name.
   - **Key Methods**:
     - `choose_column()`: Prompts the player to select a column to drop their disc.

### 4. `AIPlayer` (Subclass of `Player`)
   - **Purpose**: Represents the AI opponent, which makes automated moves using a lookahead strategy.
   - **Key Methods**:
     - `choose_column()`: The AI evaluates the game board by simulating potential moves and selecting the column that maximizes its chances of winning or minimizes the player's chances. This is achieved by looking ahead and evaluating the state of the board after each potential move.

## AI Player

The **AI player** uses a **lookahead strategy** to evaluate the best move. It simulates the outcome of future moves and selects the column that maximizes its chances of winning or minimizes the opponent's chances. The AI performs the following steps:

1. It looks ahead a few moves into the future.
2. For each possible move, it evaluates the resulting game state.
3. It assigns a score to each potential move based on how favorable it is, considering factors like potential wins, blocking the opponent, and creating opportunities.
4. The AI selects the move with the best score.

This lookahead strategy ensures that the AI is far more challenging than a simple random-move AI. 

### Example of AI Behavior:

- **Lookahead**: The AI evaluates multiple future moves and chooses the one with the highest potential.
- **Strategic Blocking**: The AI will prioritize blocking the opponent's winning moves while also trying to create opportunities for itself.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
