from IPython.display import clear_output

test_board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']

def main_view(board):

    print(' ', ' ', ' ','|',' ', ' ', ' ','|'' ', ' ', ' ',)
    print(' ',board[7],' ','|',' ',board[8],' ','|',' ',board[9],' ')
    print(' ', ' ', ' ', '|', ' ', ' ', ' ', '|'' ', ' ', ' ', )
    print('-'*21)
    print(' ', ' ', ' ', '|', ' ', ' ', ' ', '|'' ', ' ', ' ', )
    print(' ', board[4], ' ', '|', ' ', board[5], ' ', '|', ' ', board[6], ' ')
    print(' ', ' ', ' ', '|', ' ', ' ', ' ', '|'' ', ' ', ' ', )
    print('-' * 21)
    print(' ', ' ', ' ', '|', ' ', ' ', ' ', '|'' ', ' ', ' ', )
    print(' ', board[1], ' ', '|', ' ', board[2], ' ', '|', ' ', board[3], ' ')
    print(' ', ' ', ' ', '|', ' ', ' ', ' ', '|'' ', ' ', ' ', )
    return None


def player_marker_choice():
    #clear_output()

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

    return (player1,player2)



def player1_input_choice():

    choice = 's'
    acceptable_range = range(1,10)
    accept = False


    while choice.isdigit() == False or accept == False:

        choice = input('Player 1, Please select a value from 1-9: ' )

        if choice.isdigit() == False:
            print('Sorry your input is not a digit')


        if choice.isdigit() == True:
            if int(choice) in acceptable_range:
                accept = True
            else:
                print('Sorry, your input is out of range 1 to 9')
                accept = False

    return int(choice)

def player1_replacement_choice(test_board,player_marker1):


    accept = False
    myinput = 'WRONG'
    acceptable_range = range(1,10)

    while myinput.isdigit() == False and accept == False:
        choice = input('Player 1,Please select an input value 1-9: ')

        if choice.isdigit() == False:
            print('Sorry your input is not a digit')


        if choice.isdigit() == True:
            if int(choice) in acceptable_range:
                accept = True
            else:
                print('Sorry, your input is out of range 1 to 9')
                accept = False

    return int(choice)

def player2_replacement_choice(test_board,player_marker2):


    accept = False
    myblank = False
    myinput = 'WRONG'
    acceptable_range = range(1,10)


    while myinput.isdigit() == False and accept == False:
        choice = input('Player 2, Please select an input value 1-9: ')

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
player_marker1,player_marker2 = player_marker_choice()
c = player2_replacement_choice(test_board,player_marker2)
print(c)
def game_replacement(test_board,player_marker,position):

    test_board[position] = player_marker

    return test_board

def gameon_choice():
    choice = 'decision'


    while choice != ['Y','N']:
        choice = input('Do you want to play again. Choose Y or N')

        if choice not in ['Y','N']:
            clear_output()
            print('Sorry, I dont understand')


    if choice == 'Y':
        return True
    else:
        return False


game_on = True


board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']

while game_on == True:
    clear_output()

    player_marker1,player_marker2 = player_marker_choice()
    main_view(board)
    while game_on:
        print('\n'*5)

        position = player1_replacement_choice(board,player_marker1)
        board = game_replacement(board,player_marker1,position)
        main_view(board)
        position = player2_replacement_choice(board,player_marker2)
        board = game_replacement(board, player_marker2, position)
        main_view(board)



    game_on = gameon_choice()
#a = main_view(test_board)
#a = player_marker_choice()
#print(a)

d = player1_replacement_choice()
print(d)
v = player2_replacement_choice()
print(v)

b = main_view(test_board)
print(b)