# Tictactoe²

This is a basic implementation of a tictactoe² game.
The basic idea is having a tictactoe board in every field of a bigger board.

## Rules

To play one player start's by choosing a board contained in the lager board. If they are
indexed from 1-9, and the first player places his X in board 3 field 1. The second player
needs to place his O in some field in board 1 and so on. When a board is won it gets marked
by the player that won it, like in normal tictactoe. You need to win three boards in a row
to win the game. If a board 1 is won by a player and this board is selected to be placed in
the other. The current player can choose a board freely.

## Setup

The script runs in the command line using:

```
python3 tictactoe.py
```

or

```
chmod +x tictactoe.py
./tictactoe.py
```

The boards are indexed from 1 to 9 as well as the fields. The Game can be cancelled at
any point by an empty entry.
