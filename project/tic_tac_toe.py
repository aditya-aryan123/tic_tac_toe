import random

# How can I make the computer choose from a set of choices?
# I will give players the benefit that they won't select wrong choices as in case of a computer.

# Make board
# There are two ways to make a board: 1 - Manually(using 2D matrix), 2 - Using a library
board = [[' '] * 3 for i in range(3)]

# Check available moves
players_choice = []
computers_choice = []
available_choices = []
for i in range(0, 3):
    for j in range(0, 3):
        available_choices.append((i, j))

# Check win
win = None

# While condition as a stopping criteria
played = 0
while played <= 9 and win is None:

    # Players choice
    p1, p2 = map(int, input('Enter indices: ').split(' '))
    c = random.choice(available_choices)
    c1, c2 = c
    print((c1, c2), (p1, p2))

    if board[p1][p2] != ' ' or board[c1][c2] != ' ' or (c1 == p1 and c2 == p2):
        print('Invalid Play')
    else:
        if (p1, p2) in available_choices:
            available_choices.remove((p1, p2))
            players_choice.append((p1, p2))
        print(available_choices, players_choice)

        if (c1, c2) in available_choices:
            available_choices.remove((c1, c2))
            computers_choice.append((c1, c2))
        print(available_choices, computers_choice)

        # Mark the board
        board[p1][p2] = 'X'
        board[c1][c2] = 'O'
        played += 2

        rows = ['|'.join(board[r]) for r in range(3)]
        print('\n-----\n'.join(rows))

        for row in range(len(board)):
            if all(cell == 'X' for cell in board[row]):
                print("Player wins")
                win = 'X'
            elif all(cell == 'O' for cell in board[row]):
                print('Computer wins')
                win = 'O'

        for column in range(len(board[0])):
            if all(board[row][column] == 'X' for row in range(len(board))):
                print("Player wins")
                win = 'X'
            elif all(board[row][column] == 'O' for row in range(len(board))):
                print('Computer wins')
                win = 'O'

        len_column = len(board[0])

        if all(board[i][i] == 'X' for i in range(len_column)):
            print("Player wins")
            win = 'X'
        elif all(board[i][i] == 'O' for i in range(len_column)):
            print('Computer wins')
            win = 'O'

        if all(board[len_column - 1 - i][i] == 'X' for i in range(len_column - 1, -1, -1)):
            print("Player wins")
            win = 'X'
        elif all(board[len_column - 1 - i][i] == 'O' for i in range(len_column - 1, -1, -1)):
            print('Computer wins')
            win = 'O'
