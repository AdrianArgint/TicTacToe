import random

def display_board(board):
    print("\n" * 100)
    print("| " + board[0] + " | " + board[1] + " | " + board[2] + " |")
    print("| " + board[3] + " | " + board[4] + " | " + board[5] + " |")
    print("| " + board[6] + " | " + board[7] + " | " + board[8] + " |")
    pass

def player_input():
    marker = ''
    while marker != 'X' and marker != 'O':
        marker = input("Please pick a marker 'X' or 'O' for Player1: ")
    
    player1 = marker
    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'

    return (player1,player2)

def place_marker(board, marker, position):
    board[position - 1] = marker 
    pass

def win_check(board, mark):
    if board[0] == mark and board[1] == mark and board[2] == mark:
        return True
        
    if board[3] == mark and board[4] == mark and board[5] == mark:
        return True
        
    if board[6] == mark and board[7] == mark and board[8] == mark:
        return True
        
    if board[0] == mark and board[3] == mark and board[6] == mark:
        return True
        
    if board[1] == mark and board[4] == mark and board[7] == mark:
        return True
        
    if board[2] == mark and board[4] == mark and board[8] == mark:
        return True
        
    if board[0] == mark and board[4] == mark and board[8] == mark:
        return True
        
    if board[2] == mark and board[4] == mark and board[6] == mark:
        return True

    return False


def choose_first():
    if random.randint(1, 2) == 1:
        return 'Player1'

    else:
        return 'Player2'

def space_check(board, position):
    return board[position - 1] == ' '
    pass

def full_board_check(board):
    return not ' ' in board    
    pass

def player_choice(board):
    position = 0
    while True:
        try:
            position = int(input("Please enter a number: "))
        except ValueError:
            print("Sorry, please input a number between 1-9.")
            continue

        if space_check(board, position):
            break
        else:
            print("That space is not empty!") 

    return position

def replay():
    answer = input("Do you want to play again ? (Yes / No)").strip()
    return answer == 'Yes'



#Main
print('Welcome to Tic Tac Toe!')

while True:
    #Set the game up here

    board = [' '] * 9
    player1, player2 = player_input()

    turn = choose_first()
    print(turn + " will go first")

    play_game = input('Ready to play? yes or no?')

    if play_game == 'yes':
        game_on = True
    else:
        game_on = False

    while game_on:
        #Player 1`s Turn
        if turn == 'Player1':
            # Show the board
            display_board(board)
            #Choose a position
            position = player_choice(board)
            #Place the marker on the position
            place_marker(board, player1, position)
            #Check if they won
            if win_check(board,player1):
                display_board(board)
                print("PLAYER 1 HAS WON!!!")
                game_on = False
            # Or check if there is a tie
            else:
                if full_board_check(board):
                    display_board(board)
                    print("TIE GAME!")
                    game_on = False
            #No tie and no win? The next player`s turn
                else:
                    turn = "Player2"

        else:
             # Show the board
            display_board(board)
            #Choose a position
            position = player_choice(board)
            #Place the marker on the position
            place_marker(board, player2, position)
            #Check if they won
            if win_check(board,player2):
                display_board(board)
                print("PLAYER 2 HAS WON!!!")
                game_on = False
            # Or check if there is a tie
            else:
                if full_board_check(board):
                    display_board(board)
                    print("TIE GAME!")
                    game_on = False
            #No tie and no win? The next player`s turn
                else:
                    turn = "Player1"

    if not replay():
        break