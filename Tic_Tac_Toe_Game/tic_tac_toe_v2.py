from IPython.display import clear_output

test_board = ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']


def main_view(board):

    clear_output()
    print(' ', ' ', ' ', '|', ' ', ' ', ' ', '|'' ', ' ', ' ', )
    print(' ', board[7], ' ', '|', ' ', board[8], ' ', '|', ' ', board[9], ' ')
    print(' ', ' ', ' ', '|', ' ', ' ', ' ', '|'' ', ' ', ' ', )
    print('-' * 21)
    print(' ', ' ', ' ', '|', ' ', ' ', ' ', '|'' ', ' ', ' ', )
    print(' ', board[4], ' ', '|', ' ', board[5], ' ', '|', ' ', board[6], ' ')
    print(' ', ' ', ' ', '|', ' ', ' ', ' ', '|'' ', ' ', ' ', )
    print('-' * 21)
    print(' ', ' ', ' ', '|', ' ', ' ', ' ', '|'' ', ' ', ' ', )
    print(' ', board[1], ' ', '|', ' ', board[2], ' ', '|', ' ', board[3], ' ')
    print(' ', ' ', ' ', '|', ' ', ' ', ' ', '|'' ', ' ', ' ', )
    return None


def player_marker_choice():


    print('<Hello, and welcome to a Tic Tac Toe Game>')
    # Ask a player 1 to chose X or O
    marker = ''
    while marker != 'X' and marker != 'O':
        marker = input('Player 1 please choose your marker X or O: ')

    # Define player1 and player2 choices
    player1 = marker
    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'

    return (player1, player2)


def player_replacement_choice(test_board, player_marker):
    accept = False
    myinput = 'WRONG'
    acceptable_range = range(1, 10)

    while myinput.isdigit() == False and accept == False:
        choice = input('Player, Please select an input value 1-9: ')

        if choice.isdigit() == False:
            print('Sorry your input is not a digit')

        if choice.isdigit() == True:
            if int(choice) in acceptable_range:
                if test_board[int(choice)] == ' ':
                    accept = True
                else:
                    print('This place is already done')
            else:
                print('Sorry, your input is out of range 1 to 9')
                accept = False

    return int(choice)


def game_replacement(test_board, player_marker, position):
    test_board[position] = player_marker

    return test_board


def gameon_choice():
    choice = 'decision'

    while choice != ['Y', 'N']:
        choice = input('Do you want to play again. Choose Y or N: ')

        if choice not in ['Y', 'N']:
            print('Sorry, I don`t understand')

    if choice == 'Y':
        return True
    else:
        return False


def win(board):



    if test_board[1] == 'X' and test_board[2] == 'X' and test_board[3] == 'X':
        print('Congratulations, you won')
        return  True
    elif test_board[4] == 'X' and test_board[5] == 'X' and test_board[6] == 'X':
        print('Congratulations, you won')
        return  True
    elif test_board[7] == 'X' and test_board[8] == 'X' and test_board[9] == 'X':
        print('Congratulations, you won')
        return  True
    elif test_board[1] == 'X' and test_board[5] == 'X' and test_board[9] == 'X':
        print('Congratulations, you won')
        return True
    elif test_board[3] == 'X' and test_board[5] == 'X' and test_board[7] == 'X':
        print('Congratulations, you won')
        return  True
    if test_board[1] == 'O' and test_board[2] == 'O' and test_board[3] == 'O':
        print('Congratulations, you won')
        return  True
    elif test_board[4] == 'O' and test_board[5] == 'O' and test_board[6] == 'O':
        print('Congratulations, you won')
        return  True
    elif test_board[7] == 'O' and test_board[8] == 'O' and test_board[9] == 'O':
        print('Congratulations, you won')
        return  True
    elif test_board[1] == 'O' and test_board[5] == 'O' and test_board[9] == 'O':
        print('Congratulations, you won')
        return  True
    elif test_board[3] == 'O' and test_board[5] == 'O' and test_board[7] == 'O':
        print('Congratulations, you won')
        return  True
    elif test_board[1] == 'O' and test_board[4] == 'O' and test_board[7] == 'O':
        print('Congratulations, you won')
        return  True
    elif test_board[3] == 'O' and test_board[6] == 'O' and test_board[9] == 'O':
        print('Congratulations, you won')
        return  True
    elif test_board[1] == 'X' and test_board[4] == 'X' and test_board[7] == 'X':
        print('Congratulations, you won')
        return  True
    elif test_board[3] == 'X' and test_board[6] == 'X' and test_board[9] == 'X':
        print('Congratulations, you won')
        return  True
    elif test_board[2] == 'X' and test_board[5] == 'X' and test_board[8] == 'X':
        print('Congratulations, you won')
        return  True
    elif test_board[2] == 'O' and test_board[5] == 'O' and test_board[8] == 'O':
        print('Congratulations, you won')
        return  True
    elif test_board[0] != ' ' and test_board[1] != ' ' and test_board[2] != ' ' and test_board[3] != ' ' and test_board[4] != 'O' and test_board[5] != ' ' and test_board[6] != 'O' and test_board[7] != 'O' and test_board[8] != ' ' and test_board[9] != 'O':
        print('DRAW')
        return  True
    else:
        return  False






game_on = True

while game_on == True:

    player_marker1, player_marker2 = player_marker_choice()

    main_view(test_board)

    wii = False

    while wii == False:


        # Player 1 step:
        step = player_replacement_choice(test_board,player_marker1)
        test_board = game_replacement(test_board,player_marker1,step)
        main_view(test_board)

        wii = win(test_board)
        if wii == True:
            break
        # Player 2 step:
        step = player_replacement_choice(test_board,player_marker2)
        test_board = game_replacement(test_board,player_marker2,step)
        main_view(test_board)

        wii = win(test_board)
        if wii == True:
            break

    game_on = gameon_choice()

    if game_on == False:
        break
