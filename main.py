'''
  @project name:Tic Tac Toe
  @Author:Rahul Aggarwal

'''

#from IPython.display import clear_output
import random

def display_board(board):
   # clear_output()
    return(print(board[1]+'|'+board[2]+'|'+board[3]+'\n'+
                 '------'+'\n'+
                 board[4]+'|'+board[5]+'|'+board[6]+'\n'+
                 '------'+'\n'+
                 board[7]+'|'+board[8]+'|'+board[9]+
                 '     '+'\n'))




def player_input():

    marker=''

    #keep asking player to choose 'X' or 'O'

    while marker!='X' and marker!='O':
        marker=input("Player 1, choose X or O:").upper()

    #Assign player2 to opp.mark

    if marker=='X':
        return ('X','O')
    else:
        return ('O','X')

def place_marker(board,marker,position):
    board[position]=marker


def win_check(board,mark):
     return ((board[1]==board[2]==board[3]==mark) or
    (board[4] == board[5] == board[6] == mark) or
    (board[7] == board[8] == board[9] == mark) or
    (board[1] == board[4] == board[7] == mark) or
    (board[2] == board[5] == board[8] == mark) or
    (board[3] == board[6] == board[9] == mark) or
    (board[1] == board[5] == board[9] == mark) or
    (board[3] == board[5] == board[7] == mark))


def choose_first():
    flip=random.randint(1,2)
    if flip==1:
        return 'player1'
    else:
        return 'player2'

def space_check(board,position):
    return board[position]==' '

def full_board_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True

def player_choice(board):
    position=0

    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):

        position=int(input('Choose a position(1-9) '))

    return position

def replay():
    choice=input("Play Again? Enter 'Yes' or 'No' ")
    return choice=='yes'


#driver of the program

print("     !!!!!!!WELCOME TO TIC TAC TOE GAME!!!!")

while True:

    the_board=[' ']*10
    player1_marker,player2_marker=player_input()
    turn=choose_first()

    print(turn+" will go first")
    print("                                              "+'\n')
    play_game=input("Ready To Play? Enter 'y' or 'n': ")
    if play_game=='y':
        game_on=True
    else:
        game_on=False

    while game_on:
        if turn=='player1':

            #show the board
            display_board(the_board)

            #choose a position
            position=player_choice(the_board)
            place_marker(the_board,player1_marker,position)

            #check if they won
            if win_check(the_board,player1_marker):
                display_board(the_board)
                print('Player1 has won!')
                game_on=False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("Tie Game!")
                    game_on=False
                else:
                    turn='player2'
        else:
            # show the board
            display_board(the_board)

            # choose a position
            position = player_choice(the_board)
            place_marker(the_board, player2_marker, position)

            # check if they won
            if win_check(the_board, player2_marker):
                display_board(the_board)
                print('Player2 has won!')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("Tie Game!")
                    game_on = False
                else:
                    turn = 'player1'

    if not replay():
        break