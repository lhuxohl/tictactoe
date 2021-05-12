#!/usr/bin/python3

import sys

player = 'O'

game = [
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ''],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ''],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ''],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ''],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ''],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ''],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ''],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ''],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '']
]


def print_game():
    for i in range(0, len(game), 3):
        print(
            game[i][0] + '|' + game[i][1] + '|' + game[i][2] + ' ║ '
            + game[i + 1][0] + '|' + game[i + 1][1] + '|' + game[i + 1][2] + ' ║ '
            + game[i + 2][0] + '|' + game[i + 2][1] + '|' + game[i + 2][2]
        )
        print(
            game[i][3] + '|' + game[i][4] + '|' + game[i][5] + ' ║ '
            + game[i + 1][3] + '|' + game[i + 1][4] + '|' + game[i + 1][5] + ' ║ '
            + game[i + 2][3] + '|' + game[i + 2][4] + '|' + game[i + 2][5]
        )
        print(
            game[i][6] + '|' + game[i][7] + '|' + game[i][8] + ' ║ '
            + game[i + 1][6] + '|' + game[i + 1][7] + '|' + game[i + 1][8] + ' ║ '
            + game[i + 2][6] + '|' + game[i + 2][7] + '|' + game[i + 2][8]
        )
        if i == 0 or i == 3:
            print('══════╬═══════╬══════')

    print()


def print_board(board):
    print(game[board][0] + '|' + game[board][1] + '|' + game[board][2])
    print(game[board][3] + '|' + game[board][4] + '|' + game[board][5])
    print(game[board][6] + '|' + game[board][7] + '|' + game[board][8])


def draw_game():
    for i in range(len(game)):
        if game[i][9] == '':
            return False
    return True


def won_game():
    if (
            (game[0][9] == player and game[1][9] == player and game[2][9] == player) or  # horizontal top
            (game[3][9] == player and game[4][9] == player and game[5][9] == player) or  # horizontal middle
            (game[6][9] == player and game[7][9] == player and game[8][9] == player) or  # horizontal bottom
            (game[0][9] == player and game[4][9] == player and game[8][9] == player) or  # diagonal topleft-bottomright
            (game[2][9] == player and game[4][9] == player and game[6][9] == player) or  # diagonal topright-bottomleft
            (game[0][9] == player and game[3][9] == player and game[6][9] == player) or  # vertical left
            (game[1][9] == player and game[4][9] == player and game[7][9] == player) or  # vertical middle
            (game[2][9] == player and game[5][9] == player and game[8][9] == player)     # vertical bottom
    ):
        return True
    return False


def done():
    if won_game():
        return True
    return False


def valid_board(board):
    if board < 0 or board > 8:
        return False
    if not game[board][9] == '':
        return False
    return True


def select_board():
    print('Please select a board:')

    temp = input()
    if temp == '':
        sys.exit()
    temp = int(temp)

    while not valid_board(temp):
        print('Not a valid board. Please try again:')

        temp = input()
        if temp == '':
            sys.exit()
        temp = int(temp)

    return temp


def valid_field(board, field):
    if game[board][field] == ' ':
        return True
    return False


def select_field(board):
    print('Please select a field:')

    temp = input()
    if temp == '':
        sys.exit()
    temp = int(temp)

    while not valid_field(board, temp):
        print('Not a valid field. Please try again:')

        temp = input()
        if temp == '':
            sys.exit()
        temp = int(temp)

    return temp


def won_board(board):
    if (
            (game[board][0] == player and game[board][1] == player and game[board][2] == player) or  # horizontal top
            (game[board][3] == player and game[board][4] == player and game[board][5] == player) or  # horizontal middle
            (game[board][6] == player and game[board][7] == player and game[board][8] == player) or  # horizontal bottom
            (game[board][0] == player and game[board][4] == player and game[board][8] == player) or  # diagonal topleft-bottomright
            (game[board][2] == player and game[board][4] == player and game[board][6] == player) or  # diagonal topright-bottomleft
            (game[board][0] == player and game[board][3] == player and game[board][6] == player) or  # vertical left
            (game[board][1] == player and game[board][4] == player and game[board][7] == player) or  # vertical middle
            (game[board][2] == player and game[board][5] == player and game[board][8] == player)     # vertical right
    ):
        for i in range(len(game[board])):
            game[board][i] = player
        return True
    return False


def draw_board(board):
    for i in range(len(game[board]) - 1):
        if game[board][i] == ' ':
            return False

    for i in range(len(game[board])):
        game[board][i] = 'D'
    return True


if __name__ == '__main__':
    selected_board = -1

    while not done():
        if player == 'X':
            player = 'O'
        else:
            player = 'X'

        print_game()

        if not valid_board(selected_board):
            selected_board = select_board()

        print('It is ', player, '\'s turn.')
        print(selected_board, 'selected.')

        print_board(selected_board)

        selected_field = select_field(selected_board)

        game[selected_board][selected_field] = player

        if won_board(selected_board):
            print('Player', player, 'won board', selected_board, '!')
        elif draw_board(selected_board):
            print('Board', selected_board, 'ended in a draw!')

        selected_board = selected_field

    if won_game():
        print(player, 'has won the game!')
    else:
        print('The game ended in a draw!')
