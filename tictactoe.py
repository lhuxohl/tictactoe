#!/usr/bin/python3

# initializing gloabl variables
player = 'X'
game = [[[[' ' for i in range(3)] for j in range(3)]
         for k in range(3)] for l in range(3)]

top = 0
left = 0
mid = 1
right = 2
bot = 2


def print_game():
    '''
    Method for printing the current game
    '''
    for i in range(3):
        for j in range(3):
            str = ''

            for k in range(3):
                for l in range(3):
                    str += game[i][k][j][l]

                    if l != 2:
                        str += '|'
                if k != 2:
                    str += u' \u2551 '

            print(str)
        if i != 2:
            print(u'\u2550\u2550\u2550\u2550\u2550\u2550\u256c\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u256c\u2550\u2550\u2550\u2550\u2550\u2550')


def print_board(cords):
    '''
    Method for printing the selected board
    :param board_x - int - x-coordinate of board
    :param board_y - int - y-coordinate of board
    '''
    board_x = cords[0]
    board_y = cords[1]
    for j in range(3):
        str = ''
        for l in range(3):
            str += game[board_x][board_y][j][l]

            if l != 2:
                str += '|'
        print(str)


def convert_coords_to_input(coords):
    '''
    Method that converts coord back to input value
    :param coords - tuple - coords
    :return - int - input value
    '''
    switcher = {
        (2, 0): 1,
        (2, 1): 2,
        (2, 2): 3,
        (1, 0): 4,
        (1, 1): 5,
        (1, 2): 6,
        (0, 0): 7,
        (0, 1): 8,
        (0, 2): 9
    }

    return switcher.get(coords)


def convert_input_to_coords(input):
    '''
    Method that converts input value to board coordinates
    :param input - int - number input
    :returns - tuple - x- and y-coordinate of board
    '''
    switcher = {
        1: (2, 0),
        2: (2, 1),
        3: (2, 2),
        4: (1, 0),
        5: (1, 1),
        6: (1, 2),
        7: (0, 0),
        8: (0, 1),
        9: (0, 2)
    }

    if (not (input in switcher.keys())):
        return -1
    return switcher.get(input)


def board_won(board):
    '''
    Checks if the given board is won by any player
    :param board - [[String]] - current board
    :return - bool - board won
    '''
    if board_won_by_player(board, 'X') or board_won_by_player(board, 'O'):
        return True

    return False


def board_won_by_player(board, player):
    '''
    Checks if the given board is won by any player
    :param board - [[String]] - current board
    :param player - String - selected player
    :return - bool - board won by player
    '''
    if (
        board[top][left] == player and board[top][mid] == player and board[top][right] == player or
        board[mid][left] == player and board[mid][mid] == player and board[mid][right] == player or
        board[bot][left] == player and board[bot][mid] == player and board[bot][right] == player or
        board[top][left] == player and board[mid][left] == player and board[bot][left] == player or
        board[top][mid] == player and board[mid][mid] == player and board[bot][mid] == player or
        board[top][right] == player and board[mid][right] == player and board[bot][right] == player or
        board[top][left] == player and board[mid][mid] == player and board[bot][right] == player or
        board[bot][left] == player and board[mid][mid] == player and board[top][right] == player
    ):
        return True

    return False


def board_draw(board):
    '''
    Checks if a board ended in a draw
    :param board - [[String]] - current board
    :return - bool - board ended in a draw
    '''
    if not board_won(board):
        for i in range(3):
            for k in range(3):
                if board[i][k] == ' ':
                    return False
        return True
    return False


def is_valid_board(cords):
    '''
    Checks if a selected board is a valid selection
    :return - bool - selected board valid
    '''

    if cords == -1:
        return False

    board_x = cords[0]
    board_y = cords[1]
    if board_won(game[board_x][board_y]) or board_draw(game[board_x][board_y]):
        return False

    return True


def game_won():
    '''
    Checks if the game was won by either player
    '''
    if (
        board_won(game[top][left]) and board_won(game[top][mid]) and board_won(game[top][right]) or
        board_won(game[mid][left]) and board_won(game[mid][mid]) and board_won(game[mid][right]) or
        board_won(game[bot][left]) and board_won(game[bot][mid]) and board_won(game[bot][right]) or
        board_won(game[top][left]) and board_won(game[mid][left]) and board_won(game[bot][left]) or
        board_won(game[top][mid]) and board_won(game[mid][mid]) and board_won(game[bot][mid]) or
        board_won(game[top][right]) and board_won(game[mid][right]) and board_won(game[bot][right]) or
        board_won(game[top][left]) and board_won(game[mid][mid]) and board_won(game[bot][right]) or
        board_won(game[top][right]) and board_won(
            game[mid][mid]) and board_won(game[bot][left])
    ):
        return True

    return False


def game_draw():
    '''
    Checks if the game is a drawn
    '''
    for i in range(1, 10):
        if is_valid_board(convert_input_to_coords(i)):
            return False

    return True


def is_valid_field(board_cords, field_cords):
    '''
    Checks if the selected field is valid
    :param board_cords - tuple - board x- and y-coordinate
    :param field_cords -- tuple - field x- and y-coodinate
    :return - bool - valid field
    '''

    if field_cords == -1 or board_cords == -1:
        return False

    board_x = board_cords[0]
    board_y = board_cords[1]
    field_x = field_cords[0]
    field_y = field_cords[1]

    if game[board_x][board_y][field_x][field_y] == ' ':
        return True

    return False


def select_field(baord_cords):
    '''
    Method to select a valid field on the currently selected board
    :param board_cords - tuple - board x- and y-coordinate
    :return - tuple - valid field cords
    '''
    print('Please select a field:')

    temp = input()
    if temp == '' or temp == '\n':
        exit()

    temp = int(temp)
    temp = convert_input_to_coords(temp)

    while not is_valid_field(baord_cords, temp):
        print('Not a valid field! Please try again:')

        temp = input()

        if temp == '' or temp == '\n':
            exit()

        temp = int(temp)
        temp = convert_input_to_coords(temp)

    return temp


def select_board():
    '''
    Method to select a board.
    '''
    print('Please select a board:')

    temp = input()
    if temp == '' or temp == '\n':
        exit()

    temp = int(temp)
    temp = convert_input_to_coords(temp)

    while not is_valid_board(temp):
        print('Not a valid board! Please try again:')

        temp = input()

        if temp == '' or temp == '\n':
            exit()

        temp = int(temp)
        temp = convert_input_to_coords(temp)

    return temp


def game_over():
    '''
    Checks if the game should end.
    :return - bool - game drawn or won by either player
    '''

    return game_won() or game_draw()


if __name__ == "__main__":
    board_cords = -1

    while not game_over():
        if player == 'X':
            player = 'O'
        else:
            player = 'X'
        print(f'It is player {player}\'s turn.')
        print_game()

        if not is_valid_board(board_cords):
            board_cords = select_board()

        print(f'Board {convert_coords_to_input(board_cords)} selected.')
        print_board(board_cords)

        field_cords = select_field(board_cords)
        game[board_cords[0]][board_cords[1]
                             ][field_cords[0]][field_cords[1]] = player

        if board_won(game[board_cords[0]][board_cords[1]]):
            print(
                f'Player {player} won board {convert_coords_to_input(board_cords)}!')

        elif board_draw(game[board_cords[0]][board_cords[1]]):
            print(
                f'Board {convert_coords_to_input(board_cords)} ended in a draw!')

        board_cords = field_cords

    if game_won():
        print(f'Player {player} won the game!')
    else:
        print('The game ended in a draw!')
